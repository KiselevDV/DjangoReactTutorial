(this["webpackJsonpmainapp-ui"]=this["webpackJsonpmainapp-ui"]||[]).push([[0],{27:function(a,e,n){},28:function(a,e,n){},54:function(a,e,n){"use strict";n.r(e);var t=n(0),c=n.n(t),s=n(18),r=n.n(s),i=(n(27),n(28),n(22)),l=(n(29),n(19)),b=n.n(l),o=n(21),d=n(1);var j=function(){var a=Object(t.useState)([]),e=Object(i.a)(a,2),n=e[0],c=e[1];return Object(t.useEffect)((function(){b()({method:"GET",url:"http://127.0.0.1:8000/api/categories/"}).then((function(a){c(a.data)}))}),[]),Object(d.jsx)("div",{className:"App",children:Object(d.jsx)("nav",{className:"navbar navbar-expand-lg navbar-light bg-light",children:Object(d.jsxs)("div",{className:"container-fluid",children:[Object(d.jsx)("a",{className:"navbar-brand",href:"#",children:"Navbar"}),Object(d.jsx)("button",{className:"navbar-toggler",type:"button","data-bs-toggle":"collapse","data-bs-target":"#navbarNav","aria-controls":"navbarNav","aria-expanded":"false","aria-label":"Toggle navigation",children:Object(d.jsx)("span",{className:"navbar-toggler-icon"})}),Object(d.jsx)("div",{className:"collapse navbar-collapse",id:"navbarNav",children:Object(d.jsx)("ul",{className:"navbar-nav",children:n.map((function(a){return Object(d.jsx)("li",{className:"nav-item",children:Object(d.jsx)(o.a,{className:"nav-link",to:{pathname:"/categories/".concat(a.id),fromDashboard:!1},children:a.name})})}))})})]})})})};var v=function(){return Object(d.jsx)("div",{className:"App",children:Object(d.jsx)(j,{})})},u=function(a){a&&a instanceof Function&&n.e(3).then(n.bind(null,55)).then((function(e){var n=e.getCLS,t=e.getFID,c=e.getFCP,s=e.getLCP,r=e.getTTFB;n(a),t(a),c(a),s(a),r(a)}))};r.a.render(Object(d.jsx)(c.a.StrictMode,{children:Object(d.jsx)(v,{})}),document.getElementById("root")),u()}},[[54,1,2]]]);
//# sourceMappingURL=main.e19110ad.chunk.js.map