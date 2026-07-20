## AuthKitUIMacHelper

> `/System/iOSSupport/System/Library/PrivateFrameworks/AuthKitUIMacHelper.framework/Versions/A/AuthKitUIMacHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-554.0.0.0.0
-  __TEXT.__text: 0x4528
-  __TEXT.__objc_methlist: 0x5b4
+555.0.0.0.0
+  __TEXT.__text: 0x46d4
+  __TEXT.__objc_methlist: 0x5bc
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x310
   __TEXT.__oslogstring: 0x251

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x350
+  __DATA_CONST.__objc_selrefs: 0x390
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__got: 0xc8
   __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0x1e0
   __AUTH_CONST.__objc_const: 0xeb8

   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 105
-  Symbols:   391
+  Functions: 106
+  Symbols:   401
   CStrings:  39
 
Symbols:
+ -[AKAuthorizationRVSWindowController windowDidLoad]
+ _NSWorkspaceWillPowerOffNotification
+ _OBJC_CLASS_$_NSWorkspace
+ _objc_msgSend$addObserver:selector:name:object:
+ _objc_msgSend$notificationCenter
+ _objc_msgSend$removeObserver:name:object:
+ _objc_msgSend$setStyleMask:
+ _objc_msgSend$setTitleVisibility:
+ _objc_msgSend$sharedWorkspace
+ _objc_msgSend$styleMask
Functions:
~ -[AKPromptWindowController _presentAsModalWithCompletion:] : 276 -> 392
~ -[AKPromptWindowController _dimissPrompt] : 280 -> 392
+ -[AKAuthorizationRVSWindowController windowDidLoad]
```
