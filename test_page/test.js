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
    setInterval(function (){
        ArrayBufferClient.request('http://localhost:8000/bam/test/PH0745_C/0/1000',
            function(data) {
                console.log(data);
            },
            function() {
                console.log('error');
            }
        );
    },1000);
});
