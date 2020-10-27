const $source1 = document.querySelector('#source1');
const $result1 = document.querySelector('#result1');

    const typeHandler = function(e) {
        $result1.innerHTML = e.target.value;
        console.log(e.target.value);

        $.ajax({
            url: "/typos",
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
                $( "#source1" ).autocorrect({
                    source1: _
                });
            }
        });
    }

$source1.addEventListener('input', typeHandler) // register for oninput
