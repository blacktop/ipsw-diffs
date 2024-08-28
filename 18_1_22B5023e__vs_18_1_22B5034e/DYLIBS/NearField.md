## NearField

> `/System/Library/PrivateFrameworks/NearField.framework/NearField`

```diff

-351.1.0.0.0
-  __TEXT.__text: 0xa3414
+351.4.0.0.0
+  __TEXT.__text: 0xa8010
   __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_methlist: 0x53c0
+  __TEXT.__objc_methlist: 0x55a8
   __TEXT.__const: 0x247
-  __TEXT.__cstring: 0x66fd
-  __TEXT.__oslogstring: 0x4fc9
+  __TEXT.__cstring: 0x68c6
+  __TEXT.__oslogstring: 0x5302
   __TEXT.__dlopen_cstrs: 0x10c
-  __TEXT.__unwind_info: 0x1a60
-  __TEXT.__objc_classname: 0xf25
-  __TEXT.__objc_methname: 0xd1bb
-  __TEXT.__objc_methtype: 0x3674
-  __TEXT.__objc_stubs: 0x7c40
-  __DATA_CONST.__got: 0x4d0
-  __DATA_CONST.__const: 0x2470
-  __DATA_CONST.__objc_classlist: 0x330
+  __TEXT.__unwind_info: 0x1b68
+  __TEXT.__objc_classname: 0xf93
+  __TEXT.__objc_methname: 0xd752
+  __TEXT.__objc_methtype: 0x38ee
+  __TEXT.__objc_stubs: 0x7e40
+  __DATA_CONST.__got: 0x4e8
+  __DATA_CONST.__const: 0x2510
+  __DATA_CONST.__objc_classlist: 0x350
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x240
+  __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3010
-  __DATA_CONST.__objc_protorefs: 0x178
-  __DATA_CONST.__objc_superrefs: 0x240
+  __DATA_CONST.__objc_selrefs: 0x3128
+  __DATA_CONST.__objc_protorefs: 0x188
+  __DATA_CONST.__objc_superrefs: 0x250
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x428
   __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__cfstring: 0x4080
-  __AUTH_CONST.__objc_const: 0xd868
-  __AUTH_CONST.__objc_intobj: 0x840
+  __AUTH_CONST.__objc_const: 0xdf00
+  __AUTH_CONST.__objc_intobj: 0x858
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0xd20
-  __DATA.__objc_ivar: 0x510
-  __DATA.__data: 0x1b00
+  __AUTH.__objc_data: 0xd70
+  __DATA.__objc_ivar: 0x520
+  __DATA.__data: 0x1c28
   __DATA.__bss: 0x40
-  __DATA_DIRTY.__objc_ivar: 0x18c
-  __DATA_DIRTY.__objc_data: 0x12c0
+  __DATA_DIRTY.__objc_ivar: 0x194
+  __DATA_DIRTY.__objc_data: 0x13b0
   __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2519
-  Symbols:   2939
-  CStrings:  4118
+  Functions: 2600
+  Symbols:   3028
+  CStrings:  4210
 
Symbols:
+ _OBJC_CLASS_$_NFCredentialSessionInterface
+ _OBJC_METACLASS_$_NFCredentialTransceiver
+ _OBJC_CLASS_$_NFCredentialSession
+ _OBJC_METACLASS_$_NFCredentialSessionInterface
+ _OBJC_CLASS_$_NFCredentialSessionCallbackInterface
+ _OBJC_METACLASS_$_NFCredentialSessionCallbackInterface
+ _OBJC_CLASS_$_NFCredentialTransceiver
+ _OBJC_METACLASS_$_NFCredentialSession
CStrings:
+ "parentSession"
+ "listAppletsAndRefreshCache:outError:"
+ "queryExtraInfoForApplets:completion:"
+ "session:fieldChanged:"
+ "Vv20@0:8B16"
+ "TB,N,GhasInvalidated,V_invalidated"
+ "listAppletsAndRefreshCache:completion:"
+ "@\"NSData\"32@0:8@\"NSData\"16^@24"
+ "startWireModeWithApplets:selectOnStart:externalAuth:completion:"
+ "setEventDelegate:"
+ "setActiveTransceiver:"
+ "Vv64@0:8@\"NSArray\"16@\"NFApplet\"24@\"NSArray\"32@\"NSData\"40Q48@?<v@?@\"NSError\">56"
+ "_eventDelegate"
+ "wiredModeTransceive:outError:"
+ "Vv64@0:8@16@24@32@40Q48@?56"
+ "startWiredModeWithIdentifiers:externalAuth:completion:"
+ "notifyHCIData:appletIdentifier:"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "indexOfObjectWithOptions:passingTest:"
+ "startCredentialSession:"
+ "B36@0:8@\"NSArray\"16B24^@28"
+ "_invalidated"
+ "_invalidateParentSession"
+ "Vv24@0:8@\"NFApplet\"16"
+ "signChallenge:outError:"
+ "startWiredModeWithApplets:selectOnStart:externalAuth:completion:"
+ "lock"
+ "startWiredModeWithApplets:externalAuth:completion:"
+ "appletExtraInfos:outError:"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Info updated"
+ "T@\"<NFCredentialSessionEvents>\",W,N,V_eventDelegate"
+ "wireModeTransceive:outError:"
+ "queryExtraInfoForApplets:outError:"
+ "setParentSession:"
+ "@\"NFCredentialSession\""
+ "listAppletsWithCachRefresh:outError:"
+ "Vv40@0:8@\"NSObject<NFCredentialSessionCallbackInterface>\"16@\"NSDictionary\"24@?<v@?@\"NSObject<NFCredentialSessionInterface>\"B@\"NSError\">32"
+ "session:didReceiveHCIData:forAppletWithIdentifier:"
+ "T{os_unfair_lock_s=I},N,V_lock"
+ "T@\"NFCredentialTransceiver\",&,N,V_activeTransceiver"
+ "@\"NFCredentialTransceiver\""
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Unexpected applet extra info found"
+ "_syncGetSessionWithError:"
+ "queueCredentialSession:sessionAttribute:completion:"
+ "Vv32@0:8@\"NSData\"16@\"NSData\"24"
+ "T@\"NFCredentialSession\",W,N,V_parentSession"
+ "setLock:"
+ "startCardEmulationWithApplets:externalAuth:completion:"
+ "NFCredentialSession"
+ "requestSETransceiverWithCompletion:"
+ "@\"NSArray\"32@0:8@\"NSArray\"16^@24"
+ "NFCredentialSessionCallbackInterface"
+ "activeTransceiver"
+ "hasInvalidated"
+ "@\"NSArray\"28@0:8B16^@20"
+ "session:didExpireAuthorizationForApplet:"
+ "transceive:outError:"
+ "Vv32@0:8@16@24"
+ "B32@?0@\"NFApplet\"8Q16^B24"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Queue server fails."
+ "setInvalidated:"
+ "_startWiredModeWithApplets:selectOnStart:externalAuth:completion:"
+ "@28@0:8B16^@20"
+ "requestApplets:selectOnStart:AIDAllowList:externalAuth:mode:completion:"
+ "_activeTransceiver"
+ "fieldChanged:"
+ "_parentSession"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Existing active transceiver found"
+ "NFCredentialTransceiver"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Invalidate active SE transceiver"
+ "invalidated"
+ "{os_unfair_lock_s=I}16@0:8"
+ "Vv28@0:8B16@?<v@?@\"NSArray\"@\"NSError\">20"
+ "eventDelegate"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) Dirty update failed; reverted to last known values"
+ "%!c(MISSING)[%!{(MISSING)public}s %!{(MISSING)public}s]:%!i(MISSING) auth expired event for applet: %!{(MISSING)public}@"
+ "@\"<NFCredentialSessionEvents>\""
+ "deleteApplets:queueServerConnection:outError:"
+ "NFCredentialSessionInterface"

```
