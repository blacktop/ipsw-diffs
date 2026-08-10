## UIKitServices

> `/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-9127.0.79.1.102
-  __TEXT.__text: 0x21400
-  __TEXT.__objc_methlist: 0x2f3c
+9127.0.84.1.102
+  __TEXT.__text: 0x21450
+  __TEXT.__objc_methlist: 0x2fac
   __TEXT.__const: 0x2d0
   __TEXT.__dlopen_cstrs: 0x2fc
   __TEXT.__cstring: 0x45f1
   __TEXT.__oslogstring: 0x671
   __TEXT.__gcc_except_tab: 0x478
-  __TEXT.__unwind_info: 0xbe8
+  __TEXT.__unwind_info: 0xbf8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17e0
+  __DATA_CONST.__objc_selrefs: 0x17f0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x760

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1008
-  Symbols:   2906
+  Functions: 1018
+  Symbols:   2917
   CStrings:  626
 
Symbols:
+ -[UISActivityContinuationAction abortForUsageViolation:]
+ -[UISFetchContentInBackgroundAction abortForUsageViolation:]
+ -[UISHandleApplicationShortcutAction abortForUsageViolation:]
+ -[UISHandleBackgroundURLSessionAction abortForUsageViolation:]
+ -[UISHandleCloudKitShareAction abortForUsageViolation:]
+ -[UISHandleRemoteNotificationAction abortForUsageViolation:]
+ -[UISIntentForwardingActionResponse abortForUsageViolation:]
+ -[UISNotificationResponseAction abortForUsageViolation:]
+ -[UISOpenURLAction abortForUsageViolation:]
+ -[UISSceneConnectionValueAction abortForUsageViolation:]
+ _objc_msgSend$abort
Functions:
+ -[UISSceneConnectionValueAction abortForUsageViolation:]
+ -[UISHandleRemoteNotificationAction abortForUsageViolation:]
+ -[UISNotificationResponseAction abortForUsageViolation:]
+ -[UISActivityContinuationAction abortForUsageViolation:]
+ -[UISHandleCloudKitShareAction abortForUsageViolation:]
+ -[UISOpenURLAction abortForUsageViolation:]
+ -[UISHandleBackgroundURLSessionAction abortForUsageViolation:]
+ -[UISIntentForwardingActionResponse abortForUsageViolation:]
+ +[UISSceneRequestOptions supportsBSXPCSecureCoding]
+ -[UISHandleApplicationShortcutAction abortForUsageViolation:]
```
