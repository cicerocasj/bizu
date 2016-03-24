//dependence: angular

app.factory("Model", function(){
    var obj = {
        list: [],
        paginator: []
    };
    obj.get_list = function(page){
        var that = this;
        var callback_success = function(response){
            that.list = response.data.results;
            that.paginator = response.data.paginator;
        }
        var callback_error = function(response){
            console.log("Erro");
        }
        for (var i = 0; i < that.paginacao.length; i++)
            if(that.paginator[i].label == page && that.paginator[i].class == "active")
                return;
        if(page == "«") page=1
        if(page == "»") page=-1
        if(page == "...") return;
        var url = "//domain/list?page=" + page;
	//ajax for url
        
    }
    return obj;
});
