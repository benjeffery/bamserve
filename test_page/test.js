require.config({
    paths: {
        'jquery': "jquery",
        datastream: "DataStream"
    },
    shim: {
        datastream: {
          exports: 'DataStream'
        }
    },
});

require(["jquery", "ArrayBufferClient"],
    function ($, ArrayBufferClient) {
    ArrayBufferClient.request('http://localhost:8000/bam',
        function(data) {
            console.log(data);
        },
        function() {
                    console.log('error');
        }
    );
});
