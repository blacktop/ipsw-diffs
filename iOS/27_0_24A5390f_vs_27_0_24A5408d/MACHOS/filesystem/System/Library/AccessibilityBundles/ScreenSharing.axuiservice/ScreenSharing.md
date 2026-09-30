## ScreenSharing

> `/System/Library/AccessibilityBundles/ScreenSharing.axuiservice/ScreenSharing`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_data`

```diff

-166.11.0.0.0
-  __TEXT.__text: 0x6614
-  __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_stubs: 0x1b20
-  __TEXT.__objc_methlist: 0xa94
-  __TEXT.__const: 0x88
+166.13.0.0.0
+  __TEXT.__text: 0x6ed0
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__objc_stubs: 0x1ca0
+  __TEXT.__objc_methlist: 0xb24
+  __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0xc4
-  __TEXT.__objc_methname: 0x1d9d
-  __TEXT.__oslogstring: 0x400
-  __TEXT.__cstring: 0x18e
-  __TEXT.__objc_classname: 0xb5
-  __TEXT.__objc_methtype: 0x74c
-  __TEXT.__unwind_info: 0x258
+  __TEXT.__objc_methname: 0x205c
+  __TEXT.__oslogstring: 0x496
+  __TEXT.__cstring: 0x1c0
+  __TEXT.__objc_classname: 0xe3
+  __TEXT.__objc_methtype: 0x885
+  __TEXT.__unwind_info: 0x280
   __DATA_CONST.__const: 0x220
-  __DATA_CONST.__cfstring: 0x360
+  __DATA_CONST.__cfstring: 0x3a0
   __DATA_CONST.__objc_classlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x2d8
-  __DATA_CONST.__got: 0x100
-  __DATA.__objc_const: 0x1d18
-  __DATA.__objc_selrefs: 0x8e0
-  __DATA.__objc_ivar: 0xc8
+  __DATA_CONST.__auth_got: 0x308
+  __DATA_CONST.__got: 0x108
+  __DATA.__objc_const: 0x1de0
+  __DATA.__objc_selrefs: 0x948
+  __DATA.__objc_ivar: 0xd8
   __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x180
+  __DATA.__data: 0x1e0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 187
-  Symbols:   149
-  CStrings:  530
+  Functions: 197
+  Symbols:   156
+  CStrings:  562
 
Symbols:
+ _CGRectIsEmpty
+ _CGRectIsNull
+ _CGRectNull
+ _OBJC_CLASS_$_AXUIClientMessenger
+ _objc_destroyWeak
+ _objc_loadWeakRetained
+ _objc_setProperty_nonatomic_copy
+ _objc_storeWeak
- _OBJC_CLASS_$_UIScreen
CStrings:
+ "@\"<SSUICursorViewControllerDisplayBoundsDelegate>\""
+ "@\"NSString\""
+ "SSUICursorSceneClientIdentifier"
+ "SSUICursorViewControllerDisplayBoundsDelegate"
+ "T@\"<SSUICursorViewControllerDisplayBoundsDelegate>\",W,N,V_displayBoundsDelegate"
+ "T@\"NSString\",C,N,V_cursorClientIdentifier"
+ "_convertRectToSceneReferenceSpace:"
+ "_cursorClientIdentifier"
+ "_displayBoundsDelegate"
+ "_lastNotifiedDisplayBounds"
+ "_notifyDisplayBoundsDelegateIfNeeded"
+ "addContentViewController:withUserInteractionEnabled:forService:forSceneClientIdentifier:"
+ "clientMessengerWithIdentifier:"
+ "currentDisplayBoundsInSceneReferenceSpace"
+ "cursorClientIdentifier"
+ "cursorViewController:didUpdateDisplayBounds:"
+ "displayBounds"
+ "displayBounds changed, notifying delegate: %s"
+ "displayBoundsDelegate"
+ "mBaseSize"
+ "pushing displayBounds %s to client"
+ "releaseBitmapContexts"
+ "resizeFrameForDisplay:screenBounds:"
+ "resizeToFit:"
+ "sendAsynchronousMessage:withIdentifier:targetAccessQueue:completion:"
+ "setActiveSceneTrackingEnabled:forSceneClientIdentifier:"
+ "setCursorClientIdentifier:"
+ "setDisplayBoundsDelegate:"
+ "slate base size changed from (%f, %f) to (%f, %f), rebuilding bitmap"
+ "v56@0:8@\"SSUICursorViewController\"16{CGRect={CGPoint=dd}{CGSize=dd}}24"
+ "v56@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24"
+ "viewDidLayoutSubviews"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}80@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48"
+ "{CGSize=\"width\"d\"height\"d}"
+ "\xb4"
+ "\xd1"
- "addContentViewController:withUserInteractionEnabled:forService:"
- "mainScreen"
- "resizeFrameForDisplay:"
- "\x94"
```
