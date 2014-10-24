require.config({
    paths: {
        'jquery': "jquery",
        'lodash': "lodash",
        datastream: "DataStream"
    },
    shim: {
        datastream: {
          exports: 'DataStream'
        }
    },
});

require(["jquery", "lodash", "ArrayBufferClient"],
    function ($, _, ArrayBufferClient) {
    ArrayBufferClient.request('http://localhost:8000/bam/test/PH0745_C/Pf3D7_02_v3/0/1000',
        function(data) {
            var out = "<pre>";
            var cumu = 0;
            for (var i=0; i < data.pos.array.length; i++){
                var space = '';
                for (var j=0; j< data.pos.array[i];j++)
                    space += ' ';
                out += (space + data.seq.array[0].slice(cumu, cumu+data.len.array[i]) + '</br>');
                cumu += data.len.array[i];
            }
            $(document.body).html(out+'</pre>');
        },
        function() {
            console.log('error');
        }
    );
});
