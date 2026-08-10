## FrontBoardServices

> `/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__lazy_load_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__auth_got`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1150.0.0.0.0
-  __TEXT.__text: 0x987d4
+1153.0.0.0.0
+  __TEXT.__text: 0x98a4c
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_methlist: 0x8638
+  __TEXT.__objc_methlist: 0x8688
   __TEXT.__const: 0x270
-  __TEXT.__cstring: 0xc079
+  __TEXT.__cstring: 0xc0b0
   __TEXT.__oslogstring: 0x3b78
   __TEXT.__gcc_except_tab: 0x1e30
-  __TEXT.__unwind_info: 0x2ac8
+  __TEXT.__unwind_info: 0x2ad8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3110
+  __DATA_CONST.__const: 0x3128
   __DATA_CONST.__objc_classlist: 0x490
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d48
+  __DATA_CONST.__objc_selrefs: 0x3d68
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x328
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__got: 0x738
   __AUTH_CONST.__const: 0x840
-  __AUTH_CONST.__cfstring: 0xa280
-  __AUTH_CONST.__objc_const: 0x100b8
+  __AUTH_CONST.__cfstring: 0xa2e0
+  __AUTH_CONST.__objc_const: 0x100f8
   __AUTH_CONST.__lazy_load_got: 0x8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x48

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4371
-  Symbols:   7893
-  CStrings:  1935
+  Functions: 4380
+  Symbols:   7902
+  CStrings:  1938
 
Symbols:
+ -[FBSSceneAction abortForUsageViolation:]
+ -[FBSSceneSettingsCore defaultWatchdogBehavior]
+ -[FBSSceneSettingsCore setDefaultWatchdogBehavior:]
+ -[FBSSceneSnapshotAction abortForUsageViolation:]
+ -[FBSSceneSnapshotRequestAction abortForUsageViolation:]
+ -[_FBSTestExitAction abortForUsageViolation:]
+ _NSStringFromFBSDefaultWatchdogBehavior
+ ___BSSafeCast
+ _objc_msgSend$abort
CStrings:
+ "FBSSceneActivityModeIsValid(activityMode)"
+ "always"
+ "never"
```
