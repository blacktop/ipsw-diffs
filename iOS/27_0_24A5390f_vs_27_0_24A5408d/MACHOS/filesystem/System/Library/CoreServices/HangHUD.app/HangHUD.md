## HangHUD

> `/System/Library/CoreServices/HangHUD.app/HangHUD`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-424.0.0.0.0
-  __TEXT.__text: 0x2f638
-  __TEXT.__auth_stubs: 0xbf0
-  __TEXT.__objc_stubs: 0x5b20
-  __TEXT.__objc_methlist: 0x3374
-  __TEXT.__const: 0x4c0
-  __TEXT.__gcc_except_tab: 0x33c
-  __TEXT.__objc_methname: 0xa797
-  __TEXT.__cstring: 0x3895
+426.0.0.0.0
+  __TEXT.__text: 0x315c0
+  __TEXT.__auth_stubs: 0xc70
+  __TEXT.__objc_stubs: 0x5c80
+  __TEXT.__objc_methlist: 0x33dc
+  __TEXT.__const: 0x4e0
+  __TEXT.__gcc_except_tab: 0x41c
+  __TEXT.__objc_methname: 0xa928
+  __TEXT.__cstring: 0x3930
   __TEXT.__objc_classname: 0x46d
-  __TEXT.__objc_methtype: 0x19f1
-  __TEXT.__oslogstring: 0x5130
-  __TEXT.__unwind_info: 0xc38
-  __DATA_CONST.__const: 0x1ad0
+  __TEXT.__objc_methtype: 0x1a3e
+  __TEXT.__oslogstring: 0x51f3
+  __TEXT.__unwind_info: 0xcc0
+  __DATA_CONST.__const: 0x1c70
   __DATA_CONST.__cfstring: 0x5300
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_arraydata: 0x180
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA_CONST.__auth_got: 0x608
-  __DATA_CONST.__got: 0x300
-  __DATA.__objc_const: 0x6ad8
-  __DATA.__objc_selrefs: 0x2140
-  __DATA.__objc_ivar: 0x620
+  __DATA_CONST.__auth_got: 0x648
+  __DATA_CONST.__got: 0x308
+  __DATA.__objc_const: 0x6c10
+  __DATA.__objc_selrefs: 0x21a8
+  __DATA.__objc_ivar: 0x63c
   __DATA.__objc_data: 0xeb0
   __DATA.__data: 0x518
-  __DATA.__bss: 0x300
+  __DATA.__bss: 0x2f8
   - /AppleInternal/Library/Frameworks/PerformanceControlKitInternal.framework/PerformanceControlKitInternal
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1532
-  Symbols:   294
-  CStrings:  3097
+  Functions: 1558
+  Symbols:   303
+  CStrings:  3127
 
Symbols:
+ _CFRunLoopRun
+ _OBJC_CLASS_$_NSPredicate
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _objc_retain_x28
+ _objc_sync_enter
+ _objc_sync_exit
CStrings:
+ "1"
+ "@\"CADisplay\""
+ "@\"HUDAnimator\""
+ "@48@0:8@16@24@32@40"
+ "@56@0:8@16@24d32@40@48"
+ "@64@0:8@16@24@32d40@48@56"
+ "@64@0:8@16@24@32d40d48@56"
+ "A"
+ "B24@?0@\"NSNumber\"8@\"NSDictionary\"16"
+ "B40@0:8@16d24d32"
+ "Failed to register for %s: 0x%x. Falling back to lazy reconciliation at hang-event time."
+ "Invalidating current HUD Context (displayId=%u). Debug description: %@"
+ "T@\"CADisplay\",&,N,V_display"
+ "T@\"CADisplay\",R,N,V_display"
+ "T@\"HUDAnimator\",W,N,V_animator"
+ "TextAnimation: updateAnimation returned NO — token stale, re-registering"
+ "[displayId=%u] A new HUD line is created for %@ with HANG start timestamp of %llu in mach absolute time. contentId:%@"
+ "[displayId=%u] Clearing %lu HUD lines @ %s"
+ "[displayId=%u] Passed 0 HUD content, removing the HUD from screen"
+ "[displayId=%u] Removed hudLines item %@"
+ "_animator"
+ "_display"
+ "_displayChangeNotifyToken"
+ "_hudContextsByDisplayId"
+ "animator"
+ "availableModes"
+ "com.apple.CoreAnimation.CAWindowServer.DisplayChanged"
+ "com.apple.HangHUD.DisplayChangeQueue"
+ "d16@?0@\"CADisplay\"8"
+ "display"
+ "displayLinkWithDisplay:target:selector:"
+ "displayType"
+ "displays"
+ "filteredArrayUsingPredicate:"
+ "initWithConditions:theme:fontSize:display:"
+ "initWithDisplay:"
+ "initWithDisplay:queue:"
+ "initWithLineState:theme:fontSize:animator:lineDelegate:"
+ "initWithNamespaceLayer:codeLayer:spacing:"
+ "initWithProcExitRecord:theme:display:lineDelegate:"
+ "initWithQueue:processName:theme:fontSize:animator:lineDelegate:"
+ "initWithRenderContext:display:queue:"
+ "initWithTitle:label:theme:fontSize:contentScale:display:"
+ "initWithValueText:unit:theme:display:"
+ "pointScale"
+ "predicateWithBlock:"
+ "setAnimator:"
+ "setDisplay:"
+ "setWithCapacity:"
+ "topMargin for displayId=%u set to %f, displayScale=%f, orientation=%@"
+ "updateDisplays"
- "@56@0:8@16@24@32d40@48"
- "@56@0:8@16@24@32d40d48"
- "A new HUD line is created for %@ with HANG start timestamp of %llu in mach absolute time. contentId:%@"
- "Clearing %lu HUD lines @ %s"
- "Invalidating current HUD Context. Debug description: %@"
- "Passed 0 HUD content, removing the HUD from screen"
- "Removed hudLines item %@"
- "_displayLinkInvalidated"
- "cachedTopMargin is set to %f where DisplayScale is %f. The orientation is %@"
- "displayLinkWithTarget:selector:"
- "hangtracer HUD context is allocated."
- "initWithConditions:theme:fontSize:"
- "initWithLineState:theme:fontSize:lineDelegate:"
- "initWithNamespaceLayer:codeLayer:"
- "initWithProcExitRecord:theme:lineDelegate:"
- "initWithQueue:processName:theme:fontSize:lineDelegate:"
- "initWithRenderContext:queue:"
- "initWithTitle:label:theme:fontSize:contentScale:"
- "initWithValueText:unit:theme:"
- "sharedAnimator"
- "v40@0:8@16d24d32"
```
