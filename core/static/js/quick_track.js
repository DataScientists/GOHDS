"use strict";
$(function(){
    var quick_track = function(){
        var self = this;
        var btn_indicator_add = $('.j_btn_indicator_add');
        var form_template = $('.j_empty_form').html();
        var total_forms = $('#id_form-TOTAL_FORMS');
        var form_container = $('.j_form_container');
        var filter_input = $('.j_indicator_filter');
        self.indicators = {};
        self.init = function(){
            $('.j_domain').each(function(){
                var domain = {
                    id: parseInt($(this).data('id'), 10),
                    name: $('.j_domain_name', $(this)).html()
                }
                $('.j_indicator').each(function(){
                    var indicator_id = parseInt($(this).data('id'), 10)
                    self.indicators[indicator_id] = {
                        id: indicator_id,
                        name: $(this).html(),
                        domain: domain
                    }
                });
            });
            btn_indicator_add.click(self.indicator_add);
            self.refresh_indicator_names();

            self.init_indicator_filter();
        }
        self.init_indicator_filter = function(){
            filter_input.keyup(self.indicator_filter_change);
        };
        self.indicator_filter_change = function(){
            var filter_value = filter_input.val().toLowerCase();
            $('.j_domain').hide();
            $('.j_indicator').each(function(){
                var indicator = $(this);
                indicator.closest('li').hide();
                var value = indicator.html().toLowerCase();
                if(value.indexOf(filter_value) > -1){
                    indicator.closest('li').show();
                    indicator.closest('.j_domain').show();
                }
            });
        }
        self.indicator_add = function(e){
            e.preventDefault();
            var $this = $(this);
            if($this.hasClass('added')) return;
            form_container.append(form_template.split('__prefix__').join(total_forms.val()))
            $('#id_form-' + total_forms.val() + '-indicator').val($this.data('id'));
            total_forms.val(parseInt(total_forms.val(), 10) + 1);
            self.refresh_indicator_names();
            $('#add_indicator_modal').modal('hide');
            filter_input.val("");
            self.indicator_filter_change();
        }
        self.refresh_indicator_names = function(){
            $('.j_indicator_row', form_container).each(function(){
                var row = $(this);
                var name_container = row.find('.j_indicator_title');
                var value_container = row.find('.j_indicator_value');
                var slider = row.find('input[type=range]');
                var input = row.find('input[type=hidden]');
                var indicator_id = parseInt(input.val(), 10);
                name_container.html(self.indicators[indicator_id].name);
                $('.j_btn_indicator_add[data-id=' + indicator_id + ']').addClass('added');
                var slider_change = function(){
                    value_container.html(slider.val());
                }
                slider.change(slider_change);
                slider_change();
            });
        }
        return self;
    };
    new quick_track().init();
});
