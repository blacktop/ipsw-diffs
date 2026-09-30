## nfcd

> `/usr/libexec/nfcd`

```diff

-351.1.0.0.0
-  __TEXT.__text: 0x25e9ac
+351.4.0.0.0
+  __TEXT.__text: 0x267ca0
   __TEXT.__auth_stubs: 0x17c0
-  __TEXT.__delay_helper: 0xec
-  __TEXT.__objc_stubs: 0xd480
-  __TEXT.__objc_methlist: 0x75fc
-  __TEXT.__const: 0x11a0
-  __TEXT.__oslogstring: 0x237df
-  __TEXT.__cstring: 0x2d655
-  __TEXT.__objc_classname: 0x1b3e
-  __TEXT.__objc_methname: 0x164ed
-  __TEXT.__objc_methtype: 0x5177
-  __TEXT.__gcc_except_tab: 0x7570
+  __TEXT.__delay_helper: 0xc8
+  __TEXT.__objc_stubs: 0xd760
+  __TEXT.__objc_methlist: 0x783c
+  __TEXT.__const: 0x11c0
+  __TEXT.__oslogstring: 0x23d09
+  __TEXT.__cstring: 0x2d993
+  __TEXT.__objc_classname: 0x1b87
+  __TEXT.__objc_methname: 0x169bb
+  __TEXT.__objc_methtype: 0x5331
+  __TEXT.__gcc_except_tab: 0x758c
   __TEXT.__dlopen_cstrs: 0x549
-  __TEXT.__unwind_info: 0x35e0
+  __TEXT.__unwind_info: 0x3668
   __DATA_CONST.__auth_got: 0xbf0
-  __DATA_CONST.__got: 0x428
-  __DATA_CONST.__const: 0x7660
+  __DATA_CONST.__got: 0x420
+  __DATA_CONST.__const: 0x7930
   __DATA_CONST.__cfstring: 0x10120
-  __DATA_CONST.__objc_classlist: 0x598
+  __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x368
+  __DATA_CONST.__objc_protolist: 0x370
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x1b0
-  __DATA_CONST.__objc_superrefs: 0x3e8
-  __DATA_CONST.__objc_intobj: 0x68a0
+  __DATA_CONST.__objc_protorefs: 0x1c0
+  __DATA_CONST.__objc_superrefs: 0x3f0
+  __DATA_CONST.__objc_intobj: 0x6c78
   __DATA_CONST.__objc_arraydata: 0x1df0
   __DATA_CONST.__objc_arrayobj: 0x378
   __DATA_CONST.__objc_dictobj: 0xf28
-  __DATA.__objc_const: 0x165a0
-  __DATA.__objc_selrefs: 0x5138
-  __DATA.__objc_ivar: 0xf20
-  __DATA.__objc_data: 0x37f0
-  __DATA.__data: 0x2990
+  __DATA.__objc_const: 0x16ad0
+  __DATA.__objc_selrefs: 0x5208
+  __DATA.__objc_ivar: 0xf4c
+  __DATA.__objc_data: 0x38e0
+  __DATA.__data: 0x29f0
   __DATA.__bss: 0x500
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4290
-  Symbols:   523
-  CStrings:  11918
+  Functions: 4351
+  Symbols:   522
+  CStrings:  12024
 
Symbols:
- _OBJC_CLASS_$_SESKeyACLChainVerifier
CStrings:
+ "NFCredentialSession queryExtraInfoForApplets:"
+ "T{os_unfair_lock_s=I},N,V_requestedAppletsLock"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) SELECT returns memory full"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Session not allowed from %!@(MISSING) (pid %!d(MISSING))"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Abort the initialization sequence"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) %!@(MISSING), mode=%!l(MISSING)u"
+ "NFCredentialSessionSuspended"
+ "NFCredentialSessionInterface"
+ "_firstFieldNotification"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Non-supported hardware"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Select command not supported: %!@(MISSING)"
+ "member:"
+ "TB,N,V_seDirty"
+ "Vv64@0:8@\"NSArray\"16@\"NFApplet\"24@\"NSArray\"32@\"NSData\"40Q48@?<v@?@\"NSError\">56"
+ "_appletSelectedInWiredMode"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Select command not supported: %!{(MISSING)public}@"
+ "seCredentialManagerAccess"
+ "TB,N,V_firstFieldNotification"
+ "_validateCAPDU:isDFSelectCommand:outError:"
+ "Routing failure: %!@(MISSING)"
+ "T@\"NSDictionary\",&,N,V_requestedApplets"
+ "@\"NSNumber\"8@?0"
+ "Invalid auth data"
+ "T@\"NFTimer\",&,N,V_firstFieldNotificationTimer"
+ "NFCredentialSession deleteApplets:"
+ "setAppletSelectedInWiredMode:"
+ "T@\"NSSet\",&,N,V_allowedAIDsListInWiredMode"
+ "setSeDirty:"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Use provided applet's AIDs for allowed list"
+ "seDirty"
+ "Vv32@0:8@16@24"
+ "TQ,N,V_mode"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Invalid auth data"
+ "Validate APDU failed %!@(MISSING)"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Assumes %!{(MISSING)public}@"
+ "notifyHCIData:appletIdentifier:"
+ "queueCredentialSession:sessionAttribute:completion:"
+ "setAllowedAIDsListInWiredMode:"
+ "Vv24@0:8@\"NFApplet\"16"
+ "setDefaultWiredModeApplet:"
+ "HCI data"
+ "_requestedAppletsLock"
+ "setFirstFieldNotificationTimer:"
+ "_startCardEmulationWithApplet:externalAuth:"
+ "_NFCredentialSession"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Not in selected state"
+ "_requestedApplets"
+ "Missing applet on wired"
+ "setRequestedAppletsLock:"
+ "listAppletsAndRefreshCache:completion:"
+ "_startWiredModeWithExternalAuth:applets:selectOnStart:"
+ "_firstFieldNotificationTimer"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "_allowedAIDsListInWiredMode"
+ "_mode"
+ "setMode:"
+ "NFCredentialSession requestApplets:externalAuth:mode:"
+ "setFirstFieldNotification:"
+ "setRequestedApplets:"
+ "Vv28@0:8B16@?<v@?@\"NSArray\"@\"NSError\">20"
+ "Vv32@0:8@\"NSData\"16@\"NSData\"24"
+ "firstFieldNotificationTimer"
+ "NFCredentialSession listAppletsAndRefreshCache:"
+ "_setupFirstFieldNotificationTimer:"
+ ">1 applet on contactless"
+ "ResultNotFound"
+ "NFCD built from (B&I) Stockholm_Base-351.4"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Failed to config wired mode"
+ "InvalidState"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Invalid entitlements, requiring credential manager access"
+ "NFCredentialSession transceive:"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) AID=%!@(MISSING) selection is not allowed"
+ "NFCredentialSessionStarted"
+ "Vv64@0:8@16@24@32@40Q48@?56"
+ "firstFieldNotification"
+ "_defaultWiredModeApplet"
+ "\x11\x15"
+ "Vv40@0:8@\"NSObject<NFCredentialSessionCallbackInterface>\"16@\"NSDictionary\"24@?<v@?@\"NSObject<NFCredentialSessionInterface>\"B@\"NSError\">32"
+ "requestApplets:selectOnStart:AIDAllowList:externalAuth:mode:completion:"
+ "{os_unfair_lock_s=I}16@0:8"
+ "T@\"NSData\",&,N,V_defaultWiredModeApplet"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Missing applet on wired"
+ "allowedAIDsListInWiredMode"
+ "requestedAppletsLock"
+ "requestedApplets"
+ "Sign Challenge Error"
+ "TB,N,V_appletSelectedInWiredMode"
+ "defaultWiredModeApplet"
+ "queryExtraInfoForApplets:completion:"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Single applet support only on contactless"
+ "Vv20@0:8B16"
+ "NFCredentialSessionCallbackInterface"
+ "NFCredentialSession signChallenge:"
+ "B40@0:8@16^B24^@32"
+ "appletSelectedInWiredMode"
- "performChainAuthIfNeededForACL:operation:auth:seHandle:seid:error:"
- "SESSETransceiver"
- "NFCD built from (B&I) Stockholm_Base-351.1"
- "resolvedAuthorization"
- "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Failed to performChainAuthIfNeededForACL %!@(MISSING) : %!@(MISSING)"
- "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Chained Auth required: %!d(MISSING) success: %!d(MISSING)"

```
