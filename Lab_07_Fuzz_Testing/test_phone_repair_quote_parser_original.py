from hypothesis import given, strategies as st
from phone_repair_quote_parser import mask_imei, parse_parts_order, parse_model

@given(st.text() | st.none())
def test_mask_imei_no_crash(s):
    # To-Do: Using try and except complete this function.
    pass

@given(st.text() | st.none())
def test_parse_parts_order_no_crash(s):
    # To-Do: Using try and except complete this function.
    pass

@given(st.text() | st.none())
def test_parse_model_no_crash(s):
    # To-Do: Using try and except complete this function.
    pass
