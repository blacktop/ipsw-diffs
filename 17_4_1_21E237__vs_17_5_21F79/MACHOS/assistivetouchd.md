## assistivetouchd

> `/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd`

```diff

-1373.9.0.0.0
-  __TEXT.__text: 0xd5e78
+1373.13.1.0.0
+  __TEXT.__text: 0xd67f8
   __TEXT.__auth_stubs: 0x1c70
-  __TEXT.__objc_stubs: 0x249c0
-  __TEXT.__objc_methlist: 0xfc50
-  __TEXT.__cstring: 0xc222
-  __TEXT.__objc_methname: 0x2d98e
-  __TEXT.__objc_classname: 0x1f77
-  __TEXT.__objc_methtype: 0x62e2
+  __TEXT.__objc_stubs: 0x24ac0
+  __TEXT.__objc_methlist: 0xfcc0
+  __TEXT.__cstring: 0xc255
+  __TEXT.__objc_methname: 0x2da86
+  __TEXT.__objc_classname: 0x1f86
+  __TEXT.__objc_methtype: 0x6342
   __TEXT.__const: 0x560
   __TEXT.__gcc_except_tab: 0x1be8
   __TEXT.__oslogstring: 0x2d8c
   __TEXT.__dlopen_cstrs: 0xc7
-  __TEXT.__unwind_info: 0x39a8
+  __TEXT.__unwind_info: 0x39a0
   __DATA_CONST.__auth_got: 0xe48
   __DATA_CONST.__got: 0xa88
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x4150
-  __DATA_CONST.__cfstring: 0x99e0
-  __DATA_CONST.__objc_classlist: 0x5f8
+  __DATA_CONST.__const: 0x4128
+  __DATA_CONST.__cfstring: 0x9a00
+  __DATA_CONST.__objc_classlist: 0x600
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x2f8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0xae8
-  __DATA_CONST.__objc_superrefs: 0x4c0
+  __DATA_CONST.__objc_classrefs: 0xaf0
+  __DATA_CONST.__objc_superrefs: 0x4c8
   __DATA_CONST.__objc_doubleobj: 0x260
   __DATA_CONST.__objc_arraydata: 0x4f8
   __DATA_CONST.__objc_arrayobj: 0x228
   __DATA_CONST.__objc_intobj: 0x660
   __DATA_CONST.__objc_dictobj: 0x1b8
-  __DATA.__objc_const: 0x1a360
-  __DATA.__objc_selrefs: 0xa090
-  __DATA.__objc_ivar: 0x1064
-  __DATA.__objc_data: 0x3bb0
+  __DATA.__objc_const: 0x1a460
+  __DATA.__objc_selrefs: 0xa0c8
+  __DATA.__objc_ivar: 0x106c
+  __DATA.__objc_data: 0x3c00
   __DATA.__data: 0x2422
   __DATA.__bss: 0x2e5
   __DATA.__common: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 6280
+  Functions: 6288
   Symbols:   1018
-  CStrings:  9957
+  CStrings:  9966
 
CStrings:
+ "\x1d\x1f\x15"
+ "%@ action: %@, shortcut: %@"
+ "@\"SCATActionItem\""
+ "@28@0:8S16@20"
+ "@52@0:8@16@24B32@36@44"
+ "SCATActionItem"
+ "T@\"NSString\",&,N,VshortcutIdentifier"
+ "T@\"SCATActionItem\",&,N,V_currentAction"
+ "Tq,N,Vaction"
+ "Unable to handle unknown action: %@ (%@). manager:%@"
+ "actionForButtonNumber:withType:"
+ "fromAction:"
+ "fromSwitch:longPress:"
+ "longPressShortcutIdentifier"
+ "setShortcutIdentifier:"
+ "shortcutIdentifier"
+ "switchControlIgnoreInvalidSwitchConfiguration"
+ "v32@0:8@\"SCATInputController\"16@\"SCATActionItem\"24"
+ "v36@0:8@\"SCATCameraInputSource\"16@\"SCATActionItem\"24B32"
+ "v40@0:8@\"SCATAccessibilityEventInputSource\"16@\"SCATActionItem\"24B32B36"
+ "v40@0:8@\"SCATHardwareInputSource\"16@\"SCATActionItem\"24B32B36"
+ "v40@0:8@\"SCATInterDeviceInputSource\"16@\"SCATActionItem\"24B32B36"
+ "v40@0:8@\"SCATMotionTrackerInputSource\"16@\"SCATActionItem\"24B32B36"
+ "v40@0:8@\"SCATRemoteControlInputSource\"16@\"SCATActionItem\"24B32B36"
+ "v40@0:8@\"SCATScreenInputSource\"16@\"SCATActionItem\"24B32B36"
+ "v40@0:8@16@24B32B36"
+ "v52@0:8@16@24B32@36@44"
+ "void SCATGetActionIdentifiersForRecipeAndSwitch(AXSwitchRecipe *__strong, AXSwitch *__strong, SCATActionItem *__strong, SCATActionItem *__strong)"
- "\x1d\x1f$"
- "@52@0:8q16q24B32@36@44"
- "Tq,N,V_currentAction"
- "Unable to handle unknown action: %lu (%@). manager:%@"
- "q28@0:8S16@20"
- "q32@0:8q16@24"
- "v32@0:8@\"SCATInputController\"16q24"
- "v32@0:8q16B24B28"
- "v36@0:8@\"SCATCameraInputSource\"16q24B32"
- "v40@0:8@\"SCATAccessibilityEventInputSource\"16q24B32B36"
- "v40@0:8@\"SCATHardwareInputSource\"16q24B32B36"
- "v40@0:8@\"SCATInterDeviceInputSource\"16q24B32B36"
- "v40@0:8@\"SCATMotionTrackerInputSource\"16q24B32B36"
- "v40@0:8@\"SCATRemoteControlInputSource\"16q24B32B36"
- "v40@0:8@\"SCATScreenInputSource\"16q24B32B36"
- "v40@0:8@16q24B32B36"
- "v40@0:8^q16^q24@32"
- "v52@0:8q16q24B32@36@44"
- "void SCATGetActionIdentifiersForRecipeAndSwitch(AXSwitchRecipe *__strong, AXSwitch *__strong, SCATAction *, SCATAction *)"

```
