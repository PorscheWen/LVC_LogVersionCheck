function TreeCtrl()
{
	// Methods 
	this.initializeDocument	= initializeDocument;
	this.InsItem			= InsItem;
	this.GenerateCode		= GenerateCode;
	this.ToggleTree			= ToggleTree;
	this.ResetItem			= ResetItem;
	this.ExpandAllTree		= ExpandAllTree;
	this.RecudeAllTree		= RecudeAllTree;
	
	// constant 
	var nCount			= 0;
	var LastRootItem	= 0;
	var ImgDir			= "./Images/";
	var ItemImg			= "./Images/html.gif";
	
	// variable
	var Doc;
	var browserVersion;	
	var id		= "";
	var Item	= new Array();
	
	
	function initializeDocument() 
	{ 
		if (document.all) { //IE4
			Doc = document.all;
			browserVersion = 1;  
			
		}else if (document.layers) { //NS4 
			Doc = document.layers;
			browserVersion = 2; 

		}else if(document.getElementById) {	//NS6
			Doc = document;
			browserVersion = 3;		
			
		}else {	//other 
			Doc = document.all;
			browserVersion = 0; 
		}
	} 	
	
	function InsItem(parentItem, description, hreference, target)
	{
		var iDepth = 0;
		var iLength = Item.length;
		
		if(parentItem == null) {
			parentItem = iLength;
		}
		
		if(Item[parentItem] != null) {
			iDepth = Item[parentItem][4];
			iDepth++;
		}
		
		Item[iLength]		= new Array();
		Item[iLength][0]	= parentItem;
		Item[iLength][1]	= description;
		Item[iLength][2]	= hreference;
		Item[iLength][3]	= target;
		Item[iLength][4]	= iDepth;
		Item[iLength][5]	= true;
		
		nCount++;
		
		return iLength;		
	}
	
	function GenerateCode()
	{
		var NextItemDepth	= 0;
		var CurItemDepth	= 0;
		
		DocWrite("<table border='0' cellpadding='0' cellspacing='0'>");

		for(var i=0; i<nCount; i++) {
			
			DocWrite("<tr id=Tree_" + i + "><td>");
			
			DocWrite("<table border='0' cellpadding='0' cellspacing='0'><tr><td>");
			DocWrite(GetSpace(i, Item[i][4], false));
			DocWrite("</td><td>");

			DocWrite("<a href='#' onfocus='this.blur()' onclick=javascript:ToggleTree('" + i + "','" + GetChildItems(i) + "')>");
				
			var TempNodeImg;
			if(GetItemCount(i, Item[i][4]) == 1) { 
				if(Item.length == 1) { TempNodeImg = "r.gif"; }
				else { TempNodeImg = "L.gif"; }
			
			} else {
				if(i == 0) { TempNodeImg = "f.gif"; }
				else { TempNodeImg = "T.gif"; }
			}
			
				
			DocWrite("<img id=TreeNodeImg_" + i + " src='" + ImgDir + TempNodeImg + "' border='0'>");		
			DocWrite("</a>");

			DocWrite("</td><td>");
			DocWrite("<img id=TreeItemImg_" + i + " src='" + ImgDir + "html.gif" + "' border='0'>");
			DocWrite("</td><td>");
			DocWrite("&nbsp;");
			
			if(Item[i][2] != "" && Item[i][2] != null) {
				DocWrite("<a href='" + Item[i][2] + "'");

				if(Item[i][3] != "undefined" && Item[i][3] != null && Item[i][3] != "") {
					DocWrite(" target='" + Item[i][3] + "'");
				}
				DocWrite(">");
			}
			
			DocWrite(Item[i][1]);
			
			if(Item[i][2] != "" && Item[i][2] != null) {
				DocWrite("</a>");
			}

			DocWrite("</td></tr></table>");	
			DocWrite("</td></tr>");
		}
		DocWrite("</table>");
		
		LastRootItem = GetRootItem(nCount-1);
	}
	
	function GetSpace(CurItem, Depth, bBlank)
	{
		var Space = "";
		
		for(var i=0; i<Depth; i++) {
			if(bBlank == false) {
				if(bHaveSameDepthChildItem(CurItem, i)) {
					Space += "<img src=" + ImgDir + "i.gif>";
				}else {
					Space += "<img src=" + ImgDir + "white.gif>";
				}
				
			}else {
				Space += "<img src=" + ImgDir + "white.gif>";
			}
		}
		
		return Space;
	}
	
	function bHaveSameDepthChildItem(CurItem, Depth)
	{
		if(CurItem < 0 || CurItem > Item.length) { return false; }
	
		var PItem		= Item[CurItem][0];
		var RootItem	= GetRootItemEx(PItem, Depth);
		
		if(GetItemCount(RootItem, Depth) >= 2) {
			return true;
		}else {
			return false;
		}
	}
	
	function GetChildItems(iNode)
	{
		var ChildItems	= "";
		var CurDepth	= Item[iNode][4];
		
		for(var i=iNode+1; i<Item.length; i++) {

			if(CurDepth >= Item[i][4]) { return ChildItems; }
			
			if(Item[i][4] > Item[iNode][4]) {
				ChildItems += i + ";"
			}
		}

		return ChildItems;
	}
	
	function ToggleTree(CurNode, NodeItem)
	{
		if(NodeItem == "") { return; }
		
		var NodeStatus;
		var arr		= new Array();
		
		arr = NodeItem.split(";");
		
		if(Item[CurNode][5] == true) {
			ToggleDisplayLayer(arr, CurNode, "none");
			Item[CurNode][5] = false;
		}else {
			ToggleDisplayLayer(arr, CurNode, "");
			Item[CurNode][5] = true;
			ResetItem(CurNode);
		}
	}
	
	function ToggleDisplayLayer(ItemArray, CurNode, Display)
	{
		var NodeImg;
		var ItemImg;
		var bShow;
		
		if(Display == "none") { bShow = false; }
		else{ bShow = true; }

		if(!bShow) {
			ItemImg = ImgDir + "folder.gif";
			
			if(GetItemCount(CurNode,Item[CurNode][4]) == 1) {
				if(GetItemCount(GetRootItemEx(CurNode, 0),0) == 1 && CurNode == 0) {
					NodeImg = ImgDir + "Rplus.gif"; 
				}else {
					NodeImg = ImgDir + "Lplus.gif"; 
				}
				
			}else {
				if(CurNode == 0) {
					NodeImg = ImgDir + "fplus.gif"; 
				}else {
					NodeImg = ImgDir + "Tplus.gif"; 
				}
			}
			
		}
		else {
			ItemImg = ImgDir + "folderopen.gif";
			
			if(GetItemCount(CurNode,Item[CurNode][4]) == 1) {
				if(GetItemCount(GetRootItemEx(CurNode, 0),0) == 1 && CurNode == 0) {
					NodeImg = ImgDir + "Rminus.gif"; 
				}else {
					NodeImg = ImgDir + "Lminus.gif"; 
				}
				
			}else {
				if(CurNode == 0) {
					NodeImg = ImgDir + "fminus.gif"; 
				}else {		
					NodeImg = ImgDir + "Tminus.gif"; 
				}
			}
		}

		for(var i=0; i<ItemArray.length-1; i++) {
			SetTreeVisible(ItemArray[i], bShow);			
			SetImgVisible(CurNode, NodeImg, 1);
			SetImgVisible(CurNode, ItemImg, 2);		
		}
	}
	
	function ResetItem(iNode)
	{
		for(var i=iNode; i<Item.length; i++) {
	
			if(!Item[i][5]) {
				var arr = new Array();
				arr = GetChildItems(i).split(";");
				
				for(var j=0; j<arr.length-1; j++) {
					SetTreeVisible(arr[j], false);
				}
			}
		}	
	}
	
	function SetTreeVisible(iItem, bShow)
	{
		if(!bShow) {
			if(browserVersion == 1) {
				Doc["Tree_" + iItem].style.display = "none";
				
			}else if(browserVersion == 3) {
				document.getElementById("Tree_" + iItem).style.display = "none";
				
			}else {
				Doc["Tree_" + iItem].visibility = "hiden";
			}
	
		}else {
			if(browserVersion == 1) {
				Doc["Tree_" + iItem].style.display = "block";
				
			}else if(browserVersion == 3) {
				Doc.getElementById("Tree_" + iItem).style.display = "";	
							
			}else {
				Doc["Tree_" + iItem].visibility = "show";
			}				
		}
	}	
	
	function SetImgVisible(iItem, ImgName, iType)
	{
		var ItemName;
		switch(iType) {
			case 1:		ItemName = "TreeNodeImg_"; break;
			case 2:		ItemName = "TreeItemImg_"; break;
			default:	ItemName = "TreeItemImg_"; break;
		}

		if(browserVersion == 3) {
			Doc.getElementById(ItemName + iItem).src = ImgName;
			
		}else {
			Doc[ItemName + iItem].src = ImgName;
		}
	}	
	
	function ExpandAllTree()
	{
		for(var i=Item.length-1; i>=0; i--) {
			Item[i][5] = false;
			ToggleTree(i, GetChildItems(i));
		}
	}
	
	function RecudeAllTree()
	{
		for(var i=Item.length-1; i>=0; i--) {
			Item[i][5] = true;
			ToggleTree(i, GetChildItems(i));
		}
	}
	
	function GetRootItem(ChildItem)
	{
		if(Item[ChildItem][4] == 0) {
			return ChildItem;
		}else {
			return GetRootItem(Item[ChildItem][0]);
		}
	}
	
	function GetRootItemEx(ChildItem, Depth)
	{
		var nItemChecked;
		var nItemCheckedBK=-1;
		nItemChecked=ChildItem;
		while(nItemCheckedBK!=nItemChecked)
		{
		  if(Item[nItemChecked][4] == Depth)
		    return nItemChecked;
		  nItemCheckedBK=nItemChecked;
		  nItemChecked=Item[nItemChecked][0];
		}
		return GetRootItem(Item[ChildItem][0], Depth);
	}
	
	function GetItemCount(CurItem, Depth)
	{
		var nRet = 0;
		
		for(var i=CurItem; i<Item.length; i++) {
			if(Item[i][4] < Depth) break;
			
			if(Item[i][4] == Depth) {
		
				nRet++;
			}
		}
		
		return nRet;
	}

	function DocWrite(strHtml)
	{
		document.write(strHtml);
	}
}

function ToggleTree(CurNode, NodeItem)
{
	m_TreeCtrl.ToggleTree(CurNode, NodeItem);
}