const $source = document.querySelector('#source');
const $result = document.querySelector('#result');

const typeHandler = function(e) {
    $result.innerHTML = e.target.value;
    console.log(e.target.value);

    $.ajax({
        url: "/method",
        type : 'POST',
        cache: false,
        data:{'data': e.target.value},
        success: function(html)
        {
            console.log(html)
            var data = html.aggregations.auto_complete.buckets
            var _ = []

            $.each(data, (index, value)=>{
                _.push(value.key)
            });
            console.log(_)
            $( "#source" ).autocomplete({
                source: _
            });
        }
    });
}

$source.addEventListener('input', typeHandler) // register for oninput