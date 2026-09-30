## AppStoreOverlays

> `/System/Library/PrivateFrameworks/AppStoreOverlays.framework/AppStoreOverlays`

```diff

-8.0.27.0.0
-  __TEXT.__text: 0x6018
+8.0.29.0.0
+  __TEXT.__text: 0x60b8
   __TEXT.__auth_stubs: 0x3f0
   __TEXT.__objc_methlist: 0xb8c
   __TEXT.__const: 0xb0
-  __TEXT.__oslogstring: 0x8ec
+  __TEXT.__oslogstring: 0x942
   __TEXT.__cstring: 0x641
   __TEXT.__gcc_except_tab: 0x6c
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__unwind_info: 0x268
   __TEXT.__objc_classname: 0x212
-  __TEXT.__objc_methname: 0x19d3
+  __TEXT.__objc_methname: 0x1a15
   __TEXT.__objc_methtype: 0x62d
-  __TEXT.__objc_stubs: 0x1480
-  __DATA_CONST.__got: 0x100
+  __TEXT.__objc_stubs: 0x1500
+  __DATA_CONST.__got: 0x108
   __DATA_CONST.__const: 0x300
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x778
+  __DATA_CONST.__objc_selrefs: 0x798
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x50
   __AUTH_CONST.__auth_got: 0x208

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1E6E4679-D5C5-3990-946F-CC68991BB1CC
+  UUID: D4F55DE9-625F-344A-A3EC-C86F13E7FF63
   Functions: 213
-  Symbols:   945
-  CStrings:  520
+  Symbols:   950
+  CStrings:  525
 
Symbols:
+ _OBJC_CLASS_$_UIApplication
+ _objc_msgSend$activationState
+ _objc_msgSend$connectedScenes
+ _objc_msgSend$containsObject:
+ _objc_msgSend$sharedApplication
Functions:
~ -[UIWindowScene(AppOverlayManager) _aso_appOverlayManager] : 144 -> 304
CStrings:
+ "Attempted to get _aso_appOverlayManager as scene was disconnecting – returning nil."
+ "activationState"
+ "connectedScenes"
+ "containsObject:"
+ "sharedApplication"

```
