/* global bootstrap: false */
//# verbose_name='專案級別'
var j_priority_choices = [
    'Highest',
    'Important',
    'Normal'
];
// # verbose_name='專案類別'
var j_category_choices = [
    '年度計畫',
    '人力精實',
    '測試自動化',
    '設備備品',
    '耗材降低',
    '包材管控',
    'Attrition降低',
    '製程改善',
    '效率提升',
    'UPH提升',
    '品質提升',
    '自動化提升',
    '報表E化',
    '節能減排',
    '工程機電',
    '其他'
];
// # verbose_name='專案狀態'
var j_status_choices = [      
    'Ongoing',
    'Pending',
    'Closed',
    'Cancel'
];
//    # verbose_name='專案開展階段'
var j_stage_choices = [    
    '立案中',
    '需求分析',
    '待排配開發',
    '開發中',
    '驗證中',
    '已上線',
    '取消'
];
//    # verbose_name='廠區'
var j_site_choices = [    
    'ALL',
    'GL',
    'ZZ PE1',
    'ZZ PE2',
    'ZZ SUR',
    'TY',
    'BZ',
    'TN'
];
//    # verbose_name='部門'
var j_department_choices = [  
    'ALL',
    'SFA',
    'IE',
    'AAE',
    'AE',
    'ME',
    'AP',
    'RF',
    'Asset',
    'PDCA',
    'MEDD',
    'CSA',
    'Support'
];
/*
var i;
for(i=0; i<j_priority_choices.length; i++) {
    console.log(j_priority_choices[i]);
};
for(i=0; i<j_category_choices.length; i++) {
    console.log(j_category_choices[i]);
}; 
for(i=0; i<j_status_choices.length; i++) {
    console.log(j_status_choices[i]);
}; 
for(i=0; i<j_stage_choices.length; i++) {
    console.log(j_stage_choices[i]);
}; 
for(i=0; i<j_site_choices.length; i++) {
    console.log(j_site_choices[i]);
}; 
for(i=0; i<j_department_choices.length; i++) {
    console.log(j_department_choices[i]);
};
*/ 
