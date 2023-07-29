import streamlit as st
import pandas as pd
from db.config import get_conexion, close_conexion

# MySql Conecction
ps_connection = get_conexion()

def get_contactos():
    with ps_connection.cursor() as cur_ps:
        cur_ps.callproc('get_contact')
        data = cur_ps.fetchall()
        columns = [desc[0].replace('c_', '') for desc in cur_ps.description]
        df = pd.DataFrame(data, columns=columns)
        df = df[[df.columns[0], df.columns[1], df.columns[2], df.columns[3]]]
        return df

def add_contacto(fullname, email, phone):
    with ps_connection.cursor() as cur_ps:
        cur_ps.callproc('ins_contact', [fullname, email, phone])
        ps_connection.commit()

def get_contact_by_id(contact_id):
    if contact_id.strip():
        with ps_connection.cursor() as cur_ps:
            cur_ps.callproc('get_contact_id', [contact_id])
            data = cur_ps.fetchall()
            return data[0] if data else None
    return None

def update_contacto(contact_id, fullname, email, phone):
    with ps_connection.cursor() as cur_ps:
        cur_ps.callproc('upd_contact', [fullname, email, phone, contact_id])
        ps_connection.commit()

def delete_contact(contact_id):
    with ps_connection.cursor() as cur_ps:
        cur_ps.callproc('del_contact', [contact_id])
        ps_connection.commit()

def main():
    st.set_page_config(
        page_title="CRUD contactos",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get help': 'https://github.com/vicogarcia16/',
            'About': "#### Disfruta esta aplicación *extremadamente* divertida!"
        }
    )
    st.markdown("<h1 style='text-align: center;'>Aplicación de Contactos</h1>", 
                 unsafe_allow_html=True)
        
    # Obtener todos los contactos y los nombres de las columnas
    df = get_contactos()

    # Mostrar la tabla sin la columna de índice
    st.write('---')
    st.header('Lista de Contactos')
     # Limitar la cantidad de filas mostradas en la tabla
    max_rows_to_show = 10
    st.dataframe(df.set_index(df.columns[0]), height=300, use_container_width=True )

    if st.button('Actualizar tabla de contactos'):
        df = get_contactos()

    # Columna 1: Agregar nuevo contacto
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('---')
        st.header('Agregar nuevo contacto')
        fullname = st.text_input('Nombre completo', key='fullname', value='')
        email = st.text_input('Email', key='email', value='')
        phone = st.text_input('Teléfono', key='phone', value='')
        

        if st.button('Agregar contacto', key='agregar'):
            add_contacto(fullname, email, phone)
            st.success('Contacto agregado satisfactoriamente')

    # Columna 2: Editar contacto
    with col2:
        st.write('---')
        st.header('Editar contacto')
        contact_id = st.text_input('ID del contacto a editar', key='contact_id_up')
        contacto = get_contact_by_id(contact_id)
        if contacto:
            st.write(f"ID: {contacto[0]}, Nombre: {contacto[1]}, Email: {contacto[2]}, Teléfono: {contacto[3]}")
            fullname = st.text_input('Nombre completo', value=contacto[1], key='fullname1')
            email = st.text_input('Email', value=contacto[2], key='email1')
            phone = st.text_input('Teléfono', value=contacto[3], key='phone1')
        
            if st.button('Actualizar contacto', key='actualizar'):
                update_contacto(contact_id, fullname, email, phone)
                st.success('Contacto actualizado satisfactoriamente')

        elif contacto is None and contact_id.strip():
            st.warning(f'El ID: {contact_id} no se encuentra en la tabla de contactos')

    # Columna 3: Eliminar contacto
    with col3:
        st.write('---')
        st.header('Eliminar contacto')
        contact_id = st.text_input('ID del contacto a eliminar', key='id_eliminado')
        if st.button('Eliminar contacto', key='eliminar'):
            delete_contact(contact_id)
            st.success('Contacto eliminado satisfactoriamente')
            

if __name__ == '__main__':
    main()
