import plotly.express as px

def line_chart(df):
    fig = px.line(df, x='Date', y='Price', markers=True)

    return fig

def bar_chart(df):
    fig = px.bar(df, x="Avg Price", y="Series", orientation='h', text="Avg Price")
    fig.update_traces(textfont_size = 16, marker_color = 'rgb(0, 0, 0)')

    return fig

