// window加载完成时
window.onload = function(){
	// 随时调整左边栏高度
	changeWidthAndHeight();

	var changePwdBtn = document.getElementById("changePwdBtn");
	var logoutBtn = document.getElementById("logoutBtn");
	var shadow = document.getElementById("shadow");
	var changePwd = document.getElementById("changePwd");
	var logout = document.getElementById("logout");
	var changePwdClose = document.getElementById("changePwdClose");
	var changePwdChange = document.getElementById("changePwdChange");
	var logoutClose = document.getElementById("logoutClose");
	var logoutYes = document.getElementById("logoutYes");
	var rightContent = document.getElementById("rightContent");

	// 左边显示当前页面
	var localUrl = window.location.href;
	var aClick = document.getElementById("leftSide").getElementsByTagName("ul")[0].getElementsByTagName("a");
	for(var i = 0 ;i < aClick.length; i++) {
		if (localUrl.indexOf(aClick[i]) >= 0) {
			aClick[i].className += " active";
		}
	}

	// 删除或修改事件
	rightContent.onclick = function() {
		// 获取事件源id
		var target = getEventTarget();
		if (target.title != "修改" && target.title != "删除") {
			return false;
		}

		var id = target.parentNode.parentNode.parentNode.id;
		// 删除事件
		if (target.title == "删除") {
			logout.getElementsByTagName("p")[0].innerHTML = "确认删除？";
			logout.style.display = "block";
			shadow.style.display = "block";

			logoutYes.onclick = function() {
				logout.style.display = "none";
				shadow.style.display = "none";
				showTip("删除成功id="+id);
			};
		}
		// 修改事件
		else {
			alert("修改");
		}
		
	};

	// 修改密码
	changePwdBtn.onclick = function() {
		changePwd.style.display = "block";
		shadow.style.display = "block";

		// 修改了密码
		changePwdChange.onclick = function() {
			// alert("修改了密码");
			changePwd.style.display = "none";
			shadow.style.display = "none";
			showTip("修改密码成功");
		};
	};

	// 退出登录
	logoutBtn.onclick = function() {
		logout.style.display = "block";
		shadow.style.display = "block";

		// 成功退出登录
		logoutYes.onclick = function() {
			logout.style.display = "none";
			shadow.style.display = "none";
			window.location.href="/backend/logout"; 
		};
	};

	// 关闭修改密码
	changePwdClose.onclick = function() {
		changePwd.style.display = "none";
		shadow.style.display = "none";
	};

	// 关闭退出登录
	logoutClose.onclick= function() {
		logout.style.display = "none";
		shadow.style.display = "none";
	};

	// 用户提示
	

};

// window大小改变时
window.onresize = function(){
	// 随时调整左边栏高度
	changeWidthAndHeight();
};

// 随时调整左边栏高度
function changeWidthAndHeight () {
	var width  = document.documentElement.clientWidth;                                               // 获取浏览器宽度
	var height = document.documentElement.clientHeight;                                              // 获取浏览器高度

	document.getElementById('leftSide').style.height = (height - 50) + "px";                         // 50是上边栏高度
	document.getElementById('rightSide').style.height = (height - 50) + "px";                        // 50是上边栏高度
	document.getElementById('rightSide').style.width = (width>=1000) ? width-225+"px" : "1000px";    // 小于1000则为1000
	document.getElementById('topSideRight').style.width = (width>=1000) ? width-225+"px" : "1000px"; // 小于1000则为1000
}

// 获取事件源
function getEventTarget(e) {
  e = e || window.event;
  return e.target || e.srcElement;
}

function showTip(tip) {
	var shadow = document.getElementById("shadow");
	var alertTip = document.getElementById("alertTip");
	alertTip.innerHTML = tip;
	alertTip.style.display = "block";
	shadow.style.display = "block";

	setTimeout(function(){
		alertTip.style.display = "none";
		shadow.style.display = "none";
	},1500);
}