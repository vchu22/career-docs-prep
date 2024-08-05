import streamlit as st

def create_row(num_rows, num_cols, elements_callbacks, *callback_args):
    """Creates a row with the specified number of columns."""
    columns = st.columns(num_cols)
    print("\n")
    print(num_rows, num_cols)
    for r in range(num_rows):
        for c in range(num_cols):
            with columns[c]:
                tp = callback_args[0][r][c]
                print(f"length {type(tp)}")
                if type(tp) == tuple:
                    elements_callbacks[r][c](*tp)
                elif type(tp) == str:
                    print(tp)
                    elements_callbacks[r][c](tp)
        print("\n")
    return columns