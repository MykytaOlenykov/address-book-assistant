def create_table_header(value, width=42):
    return f"{'-'*width}\n|{' '*(width-2)}|\n|{value:^{width-2}}|\n|{' '*(width-2)}|\n{'-'*width}\n"
