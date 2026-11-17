## DisplayFilterUIServer

> `/System/Library/AccessibilityBundles/DisplayFilterUIServer.axuiservice/DisplayFilterUIServer`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3245.8.14.0.0
-  __TEXT.__text: 0x2960
-  __TEXT.__auth_stubs: 0x3f0
-  __TEXT.__objc_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x4d4
-  __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x284
-  __TEXT.__oslogstring: 0xb
+3245.8.23.0.0
+  __TEXT.__text: 0x3288
+  __TEXT.__auth_stubs: 0x440
+  __TEXT.__objc_stubs: 0x1000
+  __TEXT.__objc_methlist: 0x56c
+  __TEXT.__const: 0x28
+  __TEXT.__cstring: 0x2b3
+  __TEXT.__objc_methname: 0x1481
+  __TEXT.__oslogstring: 0x80
   __TEXT.__objc_classname: 0xaf
-  __TEXT.__objc_methname: 0x1178
-  __TEXT.__objc_methtype: 0x4d7
-  __TEXT.__unwind_info: 0x138
-  __DATA_CONST.__const: 0x138
-  __DATA_CONST.__cfstring: 0x260
+  __TEXT.__objc_methtype: 0x4f4
+  __TEXT.__unwind_info: 0x158
+  __DATA_CONST.__const: 0x160
+  __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_arraydata: 0x18
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x200
-  __DATA_CONST.__got: 0xe8
-  __DATA.__objc_const: 0x6a0
-  __DATA.__objc_selrefs: 0x4e8
-  __DATA.__objc_ivar: 0x2c
+  __DATA_CONST.__auth_got: 0x228
+  __DATA_CONST.__got: 0x108
+  __DATA.__objc_const: 0x730
+  __DATA.__objc_selrefs: 0x5b8
+  __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 57
-  Symbols:   108
-  CStrings:  265
+  Functions: 71
+  Symbols:   117
+  CStrings:  302
 
Symbols:
+ _AXLogDisplayFilters
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_UIApplication
+ _objc_retainBlock
+ _objc_retain_x1
+ _objc_retain_x23
+ _objc_setProperty_nonatomic_copy
CStrings:
+ "@\"NSHashTable\""
+ "@\"NSMapTable\""
+ "Adding display filter overlay %p to scene %p (activationState: %ld)"
+ "B16@?0@\"UIWindowScene\"8"
+ "Removing display filter overlay %p from scene %p"
+ "T@\"NSArray\",C,N,V__filters"
+ "T@\"NSHashTable\",&,N,V__windowScenes"
+ "T@\"NSMapTable\",&,N,V__filterOverlayControllers"
+ "__filterOverlayControllers"
+ "__filters"
+ "__windowScenes"
+ "_filterOverlayControllers"
+ "_removeFilterOverlayForWindowScene:"
+ "_shouldUseScenes"
+ "_updateFilterOverlays"
+ "_updateSceneLessFilterOverlayWithFilters:"
+ "_windowScenes"
+ "activationState"
+ "addContentViewController:withUserInteractionEnabled:forService:context:userInterfaceStyle:forWindowScene:completion:"
+ "allObjects"
+ "com.apple.ClarityBoard"
+ "connectedScenes"
+ "containsObject:"
+ "init"
+ "keyEnumerator"
+ "removeObject:"
+ "removeObjectForKey:"
+ "requestScenesForService:atPreferredSceneLevel:forSceneClientIdentifier:"
+ "screen"
+ "set"
+ "setObject:forKey:"
+ "set_filterOverlayControllers:"
+ "set_filters:"
+ "set_windowScenes:"
+ "sharedApplication"
+ "weakObjectsHashTable"
+ "weakToStrongObjectsMapTable"
```
