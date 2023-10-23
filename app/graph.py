from altair import Chart
import altair as alt


def chart(df, x, y, target) -> Chart:

    result = (Chart(df, title=f"{y} by {x} for {target}").
              mark_circle().encode(x=x, y=y, tooltip=df.columns.to_list(), color=target).interactive())
    result = result.configure(background='gray', padding={"left": 50, "top": 50, "right": 50, "bottom": 50})

    zoom = alt.selection(type='interval', bind='scales')
    pan = alt.selection(type='interval', bind='scales',
                        on="[mousedown[event.altKey], window:mouseup] > window:mousemove!", encodings=['x'])
    result = result.add_params(zoom, pan)

    result = result.configure_axis(gridOpacity=0.3, titleFontSize=20)
    result = result.configure_view(continuousWidth=500, continuousHeight=500, fill='gray', stroke=None)
    result = result.configure_title(fontSize=30, color='black')

    result = result.transform_filter(
        zoom
    ).transform_filter(
        pan)
    return result
