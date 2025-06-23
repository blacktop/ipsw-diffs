## CoreWiFi

> `/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`

```diff

-976.89.4.1.0
-  __TEXT.__text: 0x162fa0
+976.99.0.0.0
+  __TEXT.__text: 0x165ac4
   __TEXT.__auth_stubs: 0x1230
-  __TEXT.__objc_methlist: 0xdef4
-  __TEXT.__const: 0x7a8
-  __TEXT.__dlopen_cstrs: 0x903
-  __TEXT.__cstring: 0x1848b
-  __TEXT.__gcc_except_tab: 0x6060
-  __TEXT.__oslogstring: 0x1555f
+  __TEXT.__objc_methlist: 0xe0a4
+  __TEXT.__const: 0x788
+  __TEXT.__dlopen_cstrs: 0x955
+  __TEXT.__cstring: 0x1a375
+  __TEXT.__gcc_except_tab: 0x60cc
+  __TEXT.__oslogstring: 0x15cf8
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x4300
-  __TEXT.__objc_classname: 0xb98
-  __TEXT.__objc_methname: 0x1f13d
-  __TEXT.__objc_methtype: 0x3020
-  __TEXT.__objc_stubs: 0x17460
+  __TEXT.__unwind_info: 0x4360
+  __TEXT.__objc_classname: 0xba1
+  __TEXT.__objc_methname: 0x1f400
+  __TEXT.__objc_methtype: 0x3056
+  __TEXT.__objc_stubs: 0x17640
   __DATA_CONST.__got: 0x6e0
-  __DATA_CONST.__const: 0x4398
+  __DATA_CONST.__const: 0x43b0
   __DATA_CONST.__objc_classlist: 0x2f8
-  __DATA_CONST.__objc_catlist: 0x28
+  __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d98
+  __DATA_CONST.__objc_selrefs: 0x6e30
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x2a8
   __DATA_CONST.__objc_arraydata: 0x18d0
   __AUTH_CONST.__auth_got: 0x928
-  __AUTH_CONST.__const: 0x23c0
-  __AUTH_CONST.__cfstring: 0x161a0
-  __AUTH_CONST.__objc_const: 0x11d30
-  __AUTH_CONST.__objc_intobj: 0x3618
+  __AUTH_CONST.__const: 0x2420
+  __AUTH_CONST.__cfstring: 0x16280
+  __AUTH_CONST.__objc_const: 0x11f00
+  __AUTH_CONST.__objc_intobj: 0x3630
   __AUTH_CONST.__objc_arrayobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x208
   __AUTH.__objc_data: 0x910
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0xf24
+  __DATA.__objc_ivar: 0xf40
   __DATA.__data: 0xb18
   __DATA.__bss: 0x178
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_ivar: 0x54
   __DATA_DIRTY.__objc_data: 0x14a0
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x248
+  __DATA_DIRTY.__bss: 0x278
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B51DD647-6166-3B6D-8407-036EB1714B48
-  Functions: 5878
-  Symbols:   928
-  CStrings:  12894
+  UUID: A9CB1DA7-4F94-3BE5-BC2D-A03E64951C34
+  Functions: 5925
+  Symbols:   931
+  CStrings:  12976
 
Symbols:
+ _CWFDeviceIsRunningOSInternalVariant
+ _CWFDeviceIsRunningSeedBuild
+ _CWFGetLinkQualityOSLog
CStrings:
+ "%@_%@_%@_%@"
+ "-[CWFAssetManager __startAssetTracking]_block_invoke"
+ "-[CWFAssetManager __startAssetTracking]_block_invoke_2"
+ "-[CWFAssetManager __stopPeriodicCheckA11]"
+ "-[CWFAssetManager activate]"
+ "-[CWFAssetManager processQueryResults:withError:]"
+ "-[CWFAssetManager processQueryResults:withError:]_block_invoke"
+ "-[CWFAssetPowerTable assetSpecifierToTrack]"
+ "-[CWFAssetSetManager __startAssetTracking]_block_invoke"
+ "-[CWFAssetSetManager __startAssetTracking]_block_invoke_2"
+ "-[CWFAssetSetManager __stopPeriodicCheckA11]"
+ "-[CWFAssetSetManager activate]"
+ "-[CWFAssetSetManager processQueryResults:withError:]"
+ "-[CWFAssetSetManager processQueryResults:withError:]_block_invoke"
+ "-[CWFDeviceDiscoveryManager _reportFaultEventForDevices:]"
+ "-[CWFXPCRequestProxy __queryMobileAssetA11:]"
+ "-[CWFXPCRequestProxy __setupEventHandlers]_block_invoke_3"
+ "="
+ "@?<v@?>16@0:8"
+ "EQ"
+ "GET POWERTABLE INFO"
+ "PTV_API_MAJOR_VERSION"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_periodicCheckA11Timer"
+ "T@\"NSString\",&,N,V_apiMajorVersion"
+ "T@\"NSString\",C,N,V_powerTableAPIMajorVersion"
+ "T@?,C,VeventHandler"
+ "WiFiLinkQuality"
+ "WiFiOTAUpdatePTDownloadOnly"
+ "WiFiUsageMonitor"
+ "[OTA] %s: About to start tracking Assets"
+ "[OTA] %s: Chipset not fully supported."
+ "[OTA] %s: Download only platform or firmware. Disabling future a11 checks and proceeding with download-only path. error = %@"
+ "[OTA] %s: Entering"
+ "[OTA] %s: Existing self.apiMajorVersion=%@, queryResults=%@, disabling future checks."
+ "[OTA] %s: Not processing queryResults=%@, existing apiMajorversion=%@"
+ "[OTA] %s: Stopping periodic check for a11 interface"
+ "[OTA] %s: Supported platform or firmware, transient error = %@"
+ "[OTA] %s: Unsupported platform or disabled FF"
+ "[OTA] %s: Unsupported platform or firmware, disabling future a11 checks. error = %@, "
+ "[OTA] %s: Valid Asset but download only support, exiting without transferring asset to hand-off folder"
+ "[OTA] %s: _periodicCheckA11Timer is nil"
+ "[OTA] %s: invalid apiMajorVersion=%@, processing queryResults=%@"
+ "[OTA] %s: powerTableAPIMajorVersion is '%@'"
+ "[OTA_SET] %s: About to start tracking Assets"
+ "[OTA_SET] %s: Download only platform or firmware. Disabling future a11 checks and proceeding with download-only path. error = %@"
+ "[OTA_SET] %s: Entering"
+ "[OTA_SET] %s: Existing self.apiMajorVersion=%@, queryResults=%@, disabling future checks."
+ "[OTA_SET] %s: Not processing queryResults=%@, existing apiMajorversion=%@"
+ "[OTA_SET] %s: Stopping periodic check for a11 interface"
+ "[OTA_SET] %s: Supported platform or firmware, transient error = %@"
+ "[OTA_SET] %s: Unsupported platform or disabled FF"
+ "[OTA_SET] %s: Unsupported platform or firmware, disabling future a11 checks. error = %@, "
+ "[OTA_SET] %s: _periodicCheckA11Timer is nil"
+ "[OTA_SET] %s: invalid apiMajorVersion=%@, processing queryResults=%@"
+ "[corewifi-PH] %{public}s (%{public}s:%u) Submitting fault event for Rapport device fetch failure: %@ usageMonitor = %@, interface = %@"
+ "[corewifi] %{public}s (%{public}s:%u) [OTA] %s: Entering"
+ "[corewifi] %{public}s (%{public}s:%u) [OTA] %s: Failed to query powerTable info, error=%@"
+ "[corewifi] %{public}s (%{public}s:%u) [OTA] %s: Found a11 interface %@"
+ "[corewifi] %{public}s (%{public}s:%u) [OTA] %s: Query Results:%@, with error:%@"
+ "[corewifi] %{public}s (%{public}s:%u) [OTA] Failed to find WiFi interface, will not start mobile assset fetch"
+ "[corewifi] %{public}s (%{public}s:%u) [nearbysync] More than %lu seconds have passed since boot"
+ "[corewifi] %{public}s (%{public}s:%u) [nearbysync] Network was not added/user-joined within the last %lu seconds"
+ "[corewifi] [nearbysync] Failed to set captive portal credentials in the keychain (error=%{public}@) for %{public}@"
+ "__periodicCheckA11"
+ "__queryMobileAssetA11:"
+ "__startAssetTracking"
+ "__stopPeriodicCheckA11"
+ "_apiMajorVersion"
+ "_interfaceForModel:"
+ "_periodicCheckA11Timer"
+ "_powerTableAPIMajorVersion"
+ "_reportFaultEventForDevices:"
+ "addFaultEvent:forInterface:at:event:"
+ "addOperationSerializedByName:block:"
+ "apiMajorVersion"
+ "en0"
+ "function isUniqueSelector(sel) {        let matches = document.querySelectorAll(`${sel}`);        return matches.length == 1;    }    function getSelectorPathForElement(elem) {    let uniqueSelector = null;    let list = [];    while (elem.parentNode) {        let sel = '';        let tmp = '';        let tagName = elem.tagName;        if (tagName) {            sel += tagName.toLowerCase();        }        let idAttr = elem.getAttribute('id');        if (idAttr) {            sel += '#'+idAttr;        }        let nameAttr = elem.getAttribute('name');        if (nameAttr) {            sel += '[name='+nameAttr+']';        }        let typeAttr = elem.getAttribute('type');        if (typeAttr) {            sel += '[type='+typeAttr+']';        }        list.unshift(sel);        tmp = list.join(' ');        if (isUniqueSelector(tmp)) {            uniqueSelector = tmp;            break;        }        list.shift();        let classAttr = elem.getAttribute('class');        if (classAttr) {            sel += '.'+classAttr.split(' ').join('.');            list.unshift(sel);            tmp = list.join(' ');            if (isUniqueSelector(tmp)) {                uniqueSelector = tmp;                break;            }            list.shift();        }        if (elem.previousElementSibling || elem.nextElementSibling) {            let sib = elem;            let nth = 0;            while (sib) {                nth++;                sib = sib.previousElementSibling;            }            sel += ':nth-child('+nth+')';            list.unshift(sel);            tmp = list.join(' ');            if (isUniqueSelector(tmp)) {                uniqueSelector = tmp;                break;            }            list.shift();        }        list.unshift(sel);        tmp = list.join(' ');        if (isUniqueSelector(tmp)) {            uniqueSelector = tmp;            break;        }        elem = elem.parentNode;    }    return uniqueSelector;}console.log('check123'); let element = document.querySelector('%@'); if (element){ console.log('check4'); let value = '%@'; if (element.type.toLowerCase() == 'checkbox'){ element.value = value; element.checked = true; element.dispatchEvent(new Event('change', { bubbles:true, composed:true, cancelable:true } )); element.dispatchEvent(new Event('click', { bubbles:true, composed:true, cancelable:true } )); } else { element.value = value; element.dispatchEvent(new Event('input', { bubbles:true, composed:true, cancelable:true } )); } }"
+ "function isUniqueSelector(sel) {        let matches = document.querySelectorAll(`${sel}`);        return matches.length == 1;    }    function getSelectorPathForElement(elem) {    let uniqueSelector = null;    let list = [];    while (elem.parentNode) {        let sel = '';        let tmp = '';        let tagName = elem.tagName;        if (tagName) {            sel += tagName.toLowerCase();        }        let idAttr = elem.getAttribute('id');        if (idAttr) {            sel += '#'+idAttr;        }        let nameAttr = elem.getAttribute('name');        if (nameAttr) {            sel += '[name='+nameAttr+']';        }        let typeAttr = elem.getAttribute('type');        if (typeAttr) {            sel += '[type='+typeAttr+']';        }        list.unshift(sel);        tmp = list.join(' ');        if (isUniqueSelector(tmp)) {            uniqueSelector = tmp;            break;        }        list.shift();        let classAttr = elem.getAttribute('class');        if (classAttr) {            sel += '.'+classAttr.split(' ').join('.');            list.unshift(sel);            tmp = list.join(' ');            if (isUniqueSelector(tmp)) {                uniqueSelector = tmp;                break;            }            list.shift();        }        if (elem.previousElementSibling || elem.nextElementSibling) {            let sib = elem;            let nth = 0;            while (sib) {                nth++;                sib = sib.previousElementSibling;            }            sel += ':nth-child('+nth+')';            list.unshift(sel);            tmp = list.join(' ');            if (isUniqueSelector(tmp)) {                uniqueSelector = tmp;                break;            }            list.shift();        }        list.unshift(sel);        tmp = list.join(' ');        if (isUniqueSelector(tmp)) {            uniqueSelector = tmp;            break;        }        elem = elem.parentNode;    }    return uniqueSelector;}var activeElement = document.activeElement; if (activeElement && activeElement.type.toLowerCase() != 'password'){ getSelectorPathForElement(activeElement); }"
+ "function isUniqueSelector(sel) {        let matches = document.querySelectorAll(`${sel}`);        return matches.length == 1;    }    function getSelectorPathForElement(elem) {    let uniqueSelector = null;    let list = [];    while (elem.parentNode) {        let sel = '';        let tmp = '';        let tagName = elem.tagName;        if (tagName) {            sel += tagName.toLowerCase();        }        let idAttr = elem.getAttribute('id');        if (idAttr) {            sel += '#'+idAttr;        }        let nameAttr = elem.getAttribute('name');        if (nameAttr) {            sel += '[name='+nameAttr+']';        }        let typeAttr = elem.getAttribute('type');        if (typeAttr) {            sel += '[type='+typeAttr+']';        }        list.unshift(sel);        tmp = list.join(' ');        if (isUniqueSelector(tmp)) {            uniqueSelector = tmp;            break;        }        list.shift();        let classAttr = elem.getAttribute('class');        if (classAttr) {            sel += '.'+classAttr.split(' ').join('.');            list.unshift(sel);            tmp = list.join(' ');            if (isUniqueSelector(tmp)) {                uniqueSelector = tmp;                break;            }            list.shift();        }        if (elem.previousElementSibling || elem.nextElementSibling) {            let sib = elem;            let nth = 0;            while (sib) {                nth++;                sib = sib.previousElementSibling;            }            sel += ':nth-child('+nth+')';            list.unshift(sel);            tmp = list.join(' ');            if (isUniqueSelector(tmp)) {                uniqueSelector = tmp;                break;            }            list.shift();        }        list.unshift(sel);        tmp = list.join(' ');        if (isUniqueSelector(tmp)) {            uniqueSelector = tmp;            break;        }        elem = elem.parentNode;    }    return uniqueSelector;}var p = new Promise(function(resolve, reject) { document.addEventListener('click', function(event){ if ((event.target.tagName.toLowerCase() == 'textarea' || event.target.tagName.toLowerCase() == 'input') && event.target.type.toLowerCase() != 'checkbox' && event.target.value == '') { resolve(getSelectorPathForElement(event.target)); } else { resolve(undefined); } }, {once:true}); }); await p; return p;"
+ "function isUniqueSelector(sel) {        let matches = document.querySelectorAll(`${sel}`);        return matches.length == 1;    }    function getSelectorPathForElement(elem) {    let uniqueSelector = null;    let list = [];    while (elem.parentNode) {        let sel = '';        let tmp = '';        let tagName = elem.tagName;        if (tagName) {            sel += tagName.toLowerCase();        }        let idAttr = elem.getAttribute('id');        if (idAttr) {            sel += '#'+idAttr;        }        let nameAttr = elem.getAttribute('name');        if (nameAttr) {            sel += '[name='+nameAttr+']';        }        let typeAttr = elem.getAttribute('type');        if (typeAttr) {            sel += '[type='+typeAttr+']';        }        list.unshift(sel);        tmp = list.join(' ');        if (isUniqueSelector(tmp)) {            uniqueSelector = tmp;            break;        }        list.shift();        let classAttr = elem.getAttribute('class');        if (classAttr) {            sel += '.'+classAttr.split(' ').join('.');            list.unshift(sel);            tmp = list.join(' ');            if (isUniqueSelector(tmp)) {                uniqueSelector = tmp;                break;            }            list.shift();        }        if (elem.previousElementSibling || elem.nextElementSibling) {            let sib = elem;            let nth = 0;            while (sib) {                nth++;                sib = sib.previousElementSibling;            }            sel += ':nth-child('+nth+')';            list.unshift(sel);            tmp = list.join(' ');            if (isUniqueSelector(tmp)) {                uniqueSelector = tmp;                break;            }            list.shift();        }        list.unshift(sel);        tmp = list.join(' ');        if (isUniqueSelector(tmp)) {            uniqueSelector = tmp;            break;        }        elem = elem.parentNode;    }    return uniqueSelector;}var p = new Promise(function(resolve, reject) { document.addEventListener('focusin', function(event){ if ((event.target.tagName.toLowerCase() == 'textarea' || event.target.tagName.toLowerCase() == 'input') && event.target.type.toLowerCase() != 'checkbox' && event.target.value == '') { resolve(getSelectorPathForElement(event.target)); } else { resolve(undefined); } }, {once:true}); }); await p; return p;"
+ "function isUniqueSelector(sel) {        let matches = document.querySelectorAll(`${sel}`);        return matches.length == 1;    }    function getSelectorPathForElement(elem) {    let uniqueSelector = null;    let list = [];    while (elem.parentNode) {        let sel = '';        let tmp = '';        let tagName = elem.tagName;        if (tagName) {            sel += tagName.toLowerCase();        }        let idAttr = elem.getAttribute('id');        if (idAttr) {            sel += '#'+idAttr;        }        let nameAttr = elem.getAttribute('name');        if (nameAttr) {            sel += '[name='+nameAttr+']';        }        let typeAttr = elem.getAttribute('type');        if (typeAttr) {            sel += '[type='+typeAttr+']';        }        list.unshift(sel);        tmp = list.join(' ');        if (isUniqueSelector(tmp)) {            uniqueSelector = tmp;            break;        }        list.shift();        let classAttr = elem.getAttribute('class');        if (classAttr) {            sel += '.'+classAttr.split(' ').join('.');            list.unshift(sel);            tmp = list.join(' ');            if (isUniqueSelector(tmp)) {                uniqueSelector = tmp;                break;            }            list.shift();        }        if (elem.previousElementSibling || elem.nextElementSibling) {            let sib = elem;            let nth = 0;            while (sib) {                nth++;                sib = sib.previousElementSibling;            }            sel += ':nth-child('+nth+')';            list.unshift(sel);            tmp = list.join(' ');            if (isUniqueSelector(tmp)) {                uniqueSelector = tmp;                break;            }            list.shift();        }        list.unshift(sel);        tmp = list.join(' ');        if (isUniqueSelector(tmp)) {            uniqueSelector = tmp;            break;        }        elem = elem.parentNode;    }    return uniqueSelector;}var p = new Promise(function(resolve, reject) { document.addEventListener('focusout', function(event){ if ((event.target.tagName.toLowerCase() == 'textarea' || event.target.tagName.toLowerCase() == 'input') && event.target.type.toLowerCase() != 'checkbox') { resolve(getSelectorPathForElement(event.target)); } else { resolve(undefined); } }, {once:true}); }); await p; return p;"
+ "function isUniqueSelector(sel) {        let matches = document.querySelectorAll(`${sel}`);        return matches.length == 1;    }    function getSelectorPathForElement(elem) {    let uniqueSelector = null;    let list = [];    while (elem.parentNode) {        let sel = '';        let tmp = '';        let tagName = elem.tagName;        if (tagName) {            sel += tagName.toLowerCase();        }        let idAttr = elem.getAttribute('id');        if (idAttr) {            sel += '#'+idAttr;        }        let nameAttr = elem.getAttribute('name');        if (nameAttr) {            sel += '[name='+nameAttr+']';        }        let typeAttr = elem.getAttribute('type');        if (typeAttr) {            sel += '[type='+typeAttr+']';        }        list.unshift(sel);        tmp = list.join(' ');        if (isUniqueSelector(tmp)) {            uniqueSelector = tmp;            break;        }        list.shift();        let classAttr = elem.getAttribute('class');        if (classAttr) {            sel += '.'+classAttr.split(' ').join('.');            list.unshift(sel);            tmp = list.join(' ');            if (isUniqueSelector(tmp)) {                uniqueSelector = tmp;                break;            }            list.shift();        }        if (elem.previousElementSibling || elem.nextElementSibling) {            let sib = elem;            let nth = 0;            while (sib) {                nth++;                sib = sib.previousElementSibling;            }            sel += ':nth-child('+nth+')';            list.unshift(sel);            tmp = list.join(' ');            if (isUniqueSelector(tmp)) {                uniqueSelector = tmp;                break;            }            list.shift();        }        list.unshift(sel);        tmp = list.join(' ');        if (isUniqueSelector(tmp)) {            uniqueSelector = tmp;            break;        }        elem = elem.parentNode;    }    return uniqueSelector;}var p = new Promise(function(resolve, reject){ document.addEventListener('keydown', function(event){ let target = event.target; let selector = getSelectorPathForElement(target); let value = target.value; var capturedData = {}; if (selector && value){ capturedData[selector] = value; } resolve(capturedData); }, { once:true }); document.addEventListener('keyup', function(event){ let target = event.target; let selector = getSelectorPathForElement(target); let value = target.value; var capturedData = {}; if (selector && value){ capturedData[selector] = value; } resolve(capturedData); }, { once:true }); document.addEventListener('input', function(event){ let target = event.target; let selector = getSelectorPathForElement(target); let value = target.value; var capturedData = {}; if (selector && value && (target.type.toLowerCase() != 'checkbox' || target.checked)){ capturedData[selector] = value; } resolve(capturedData); }, { once:true }); }); await p; return p;"
+ "ir0"
+ "isChipsetDownloadOnly"
+ "isChipsetFullySupported"
+ "isSupportedOTAPTDownloadOnly"
+ "periodicCheckA11Timer"
+ "powerTableAPIMajorVersion"
+ "powerTableInfo"
+ "powerTableInfo:"
+ "processQueryResults:withError:"
+ "queryPowerTableInfoWithRequestParams:reply:"
+ "setApiMajorVersion:"
+ "setPeriodicCheckA11Timer:"
+ "setPowerTableAPIMajorVersion:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy"
+ "stringValue"
+ "updateKnownNetwork"
+ "v24@0:8@?<v@?>16"
+ "v32@0:8@\"NSDictionary\"16@\"NSError\"24"
- "+[CWFAssetPowerTable assetSpecifierToTrack]"
- "-[CWFAssetManager startEventMonitoring]"
- "-[CWFAssetManager startEventMonitoring]_block_invoke"
- "-[CWFAssetManager startEventMonitoring]_block_invoke_2"
- "-[CWFAssetSetManager startEventMonitoring]"
- "-[CWFAssetSetManager startEventMonitoring]_block_invoke"
- "-[CWFAssetSetManager startEventMonitoring]_block_invoke_2"
- "[OTA] %s: Existing, valid localAsset but download only support"
- "[OTA] %s: OTA update of PT is disabled"
- "[OTA] %s: Unsupported platform"
- "[OTA_SET] %s: OTA update of PT is disabled"
- "[OTA_SET] %s: Unsupported platform"
- "[corewifi] %{public}s (%{public}s:%u) [nearbysync] More than %d hours have passed since boot"
- "[corewifi] %{public}s (%{public}s:%u) [nearbysync] Network was not added/user-joined within the last %d days"
- "[corewifi] [nearbysync] Failed to set captive portal credentials in the keychain (error=%{public}@), not adding (%{public}@)"
- "function getXPathForElement(element){ if (!element) { return ''; } if (element.id) { return `//*[@id=\"${element.id}\"]`; } if (element === document.body) { return '/html/body'; } let selector = ''; let tagName = element.tagName.toLowerCase(); let parentElement = element.parentElement; if (parentElement.childElementCount > 1) { let parentsChildren = [...parentElement.children]; let tag = []; parentsChildren.forEach(child => { if (child.tagName.toLowerCase() === tagName) { tag.push(child); } } ); if (tag.length === 1) { selector = tagName; } else { let position = tag.indexOf(element) + 1; selector = `${tagName}[${position}]`; } } else { selector = tagName; } return `${getXPathForElement(element.parentNode)}/${selector}`; }let xpathResult = document.evaluate('%@', document.documentElement, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null); let element = xpathResult.singleNodeValue; if (element){ let value = '%@'; if (element.type.toLowerCase() == 'checkbox'){ element.value = value; element.checked = true; element.dispatchEvent(new Event('change', { bubbles:true, composed:true, cancelable:true } )); element.dispatchEvent(new Event('click', { bubbles:true, composed:true, cancelable:true } )); } else { element.value = value; element.value = value; element.dispatchEvent(new Event('input', { bubbles:true, composed:true, cancelable:true } )); } }"
- "function getXPathForElement(element){ if (!element) { return ''; } if (element.id) { return `//*[@id=\"${element.id}\"]`; } if (element === document.body) { return '/html/body'; } let selector = ''; let tagName = element.tagName.toLowerCase(); let parentElement = element.parentElement; if (parentElement.childElementCount > 1) { let parentsChildren = [...parentElement.children]; let tag = []; parentsChildren.forEach(child => { if (child.tagName.toLowerCase() === tagName) { tag.push(child); } } ); if (tag.length === 1) { selector = tagName; } else { let position = tag.indexOf(element) + 1; selector = `${tagName}[${position}]`; } } else { selector = tagName; } return `${getXPathForElement(element.parentNode)}/${selector}`; }var activeElement = document.activeElement; if (activeElement && activeElement.type.toLowerCase() != 'password'){ getXPathForElement(activeElement); }"
- "function getXPathForElement(element){ if (!element) { return ''; } if (element.id) { return `//*[@id=\"${element.id}\"]`; } if (element === document.body) { return '/html/body'; } let selector = ''; let tagName = element.tagName.toLowerCase(); let parentElement = element.parentElement; if (parentElement.childElementCount > 1) { let parentsChildren = [...parentElement.children]; let tag = []; parentsChildren.forEach(child => { if (child.tagName.toLowerCase() === tagName) { tag.push(child); } } ); if (tag.length === 1) { selector = tagName; } else { let position = tag.indexOf(element) + 1; selector = `${tagName}[${position}]`; } } else { selector = tagName; } return `${getXPathForElement(element.parentNode)}/${selector}`; }var p = new Promise(function(resolve, reject) { document.addEventListener('click', function(event){ if ((event.target.tagName.toLowerCase() == 'textarea' || event.target.tagName.toLowerCase() == 'input') && event.target.type.toLowerCase() != 'checkbox' && event.target.value == '') { resolve(getXPathForElement(event.target)); } else { resolve(undefined); } }, {once:true}); }); await p; return p;"
- "function getXPathForElement(element){ if (!element) { return ''; } if (element.id) { return `//*[@id=\"${element.id}\"]`; } if (element === document.body) { return '/html/body'; } let selector = ''; let tagName = element.tagName.toLowerCase(); let parentElement = element.parentElement; if (parentElement.childElementCount > 1) { let parentsChildren = [...parentElement.children]; let tag = []; parentsChildren.forEach(child => { if (child.tagName.toLowerCase() === tagName) { tag.push(child); } } ); if (tag.length === 1) { selector = tagName; } else { let position = tag.indexOf(element) + 1; selector = `${tagName}[${position}]`; } } else { selector = tagName; } return `${getXPathForElement(element.parentNode)}/${selector}`; }var p = new Promise(function(resolve, reject) { document.addEventListener('focusin', function(event){ if ((event.target.tagName.toLowerCase() == 'textarea' || event.target.tagName.toLowerCase() == 'input') && event.target.type.toLowerCase() != 'checkbox' && event.target.value == '') { resolve(getXPathForElement(event.target)); } else { resolve(undefined); } }, {once:true}); }); await p; return p;"
- "function getXPathForElement(element){ if (!element) { return ''; } if (element.id) { return `//*[@id=\"${element.id}\"]`; } if (element === document.body) { return '/html/body'; } let selector = ''; let tagName = element.tagName.toLowerCase(); let parentElement = element.parentElement; if (parentElement.childElementCount > 1) { let parentsChildren = [...parentElement.children]; let tag = []; parentsChildren.forEach(child => { if (child.tagName.toLowerCase() === tagName) { tag.push(child); } } ); if (tag.length === 1) { selector = tagName; } else { let position = tag.indexOf(element) + 1; selector = `${tagName}[${position}]`; } } else { selector = tagName; } return `${getXPathForElement(element.parentNode)}/${selector}`; }var p = new Promise(function(resolve, reject) { document.addEventListener('focusout', function(event){ if ((event.target.tagName.toLowerCase() == 'textarea' || event.target.tagName.toLowerCase() == 'input') && event.target.type.toLowerCase() != 'checkbox') { resolve(getXPathForElement(event.target)); } else { resolve(undefined); } }, {once:true}); }); await p; return p;"
- "function getXPathForElement(element){ if (!element) { return ''; } if (element.id) { return `//*[@id=\"${element.id}\"]`; } if (element === document.body) { return '/html/body'; } let selector = ''; let tagName = element.tagName.toLowerCase(); let parentElement = element.parentElement; if (parentElement.childElementCount > 1) { let parentsChildren = [...parentElement.children]; let tag = []; parentsChildren.forEach(child => { if (child.tagName.toLowerCase() === tagName) { tag.push(child); } } ); if (tag.length === 1) { selector = tagName; } else { let position = tag.indexOf(element) + 1; selector = `${tagName}[${position}]`; } } else { selector = tagName; } return `${getXPathForElement(element.parentNode)}/${selector}`; }var p = new Promise(function(resolve, reject){ document.addEventListener('keydown', function(event){ let target = event.target; let selector = getXPathForElement(target); let value = target.value; var capturedData = {}; if (selector && value){ capturedData[selector] = value; } resolve(capturedData); }, { once:true }); document.addEventListener('keyup', function(event){ let target = event.target; let selector = getXPathForElement(target); let value = target.value; var capturedData = {}; if (selector && value){ capturedData[selector] = value; } resolve(capturedData); }, { once:true }); document.addEventListener('input', function(event){ let target = event.target; let selector = getXPathForElement(target); let value = target.value; var capturedData = {}; if (selector && value && (target.type.toLowerCase() != 'checkbox' || target.checked)){ capturedData[selector] = value; } resolve(capturedData); }, { once:true }); }); await p; return p;"
- "i28@0:8I16@20"
- "isSupportedChipsetDownloadOnly"
- "statusFlags"
- "updateKnownBSS"

```
