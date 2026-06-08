## HomeKitIntentExtension

> `/System/Library/Frameworks/HomeKit.framework/PlugIns/HomeKitIntentExtension.appex/HomeKitIntentExtension`

```diff

-1418.6.20.0.0
-  __TEXT.__text: 0x1478
-  __TEXT.__auth_stubs: 0x2c0
+1468.5.0.0.6
+  __TEXT.__text: 0x16a4
+  __TEXT.__auth_stubs: 0x310
   __TEXT.__objc_stubs: 0x380
   __TEXT.__objc_methlist: 0x2a4
-  __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x48
-  __TEXT.__cstring: 0x4a
-  __TEXT.__oslogstring: 0x26e
-  __TEXT.__objc_classname: 0x53
+  __TEXT.__const: 0x40
+  __TEXT.__gcc_except_tab: 0x20
+  __TEXT.__cstring: 0x4c
+  __TEXT.__oslogstring: 0x48f
+  __TEXT.__objc_classname: 0x51
   __TEXT.__objc_methname: 0x57d
   __TEXT.__objc_methtype: 0x28d
-  __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x170
-  __DATA_CONST.__got: 0x78
+  __TEXT.__unwind_info: 0xb0
   __DATA_CONST.__const: 0xb8
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__auth_got: 0x198
+  __DATA_CONST.__got: 0x78
   __DATA.__objc_const: 0x340
   __DATA.__objc_selrefs: 0x1e0
   __DATA.__objc_ivar: 0x10

   - /System/Library/Frameworks/HomeKit.framework/HomeKit
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation
-  - /System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5CFC1320-67AD-3628-BA50-21339B410E87
+  UUID: 38D0238E-8A52-3511-B5AB-1ECFA31FEA68
   Functions: 23
-  Symbols:   70
-  CStrings:  127
+  Symbols:   75
+  CStrings:  138
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x27
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_autoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
CStrings:
+ "%@ time takes too long. Timer already fired"
+ "Execution is not allowed for intent: [ %@ ]"
+ "Failed to %@ intent: [ %@ ] - error %@"
+ "HMIntentHandler has been set to nil"
+ "HomePod is not eligible for intent handling"
+ "Intent: [ %@ ] is %@ successfully"
+ "Invoking completion for intent %@ with response %@"
+ "Passed-in outcome is invalid"
+ "This intent contains unsecuring actions and needs user's authentication"
+ "This intent contains unsecuring actions but the device does not enable the passcode"
+ "Unlock required for intent: [ %@ ]"
+ "[%{public}@] %@ time takes too long. Timer already fired"
+ "[%{public}@] Execution is not allowed for intent: [ %@ ]"
+ "[%{public}@] Failed to %@ intent: [ %@ ] - error %@"
+ "[%{public}@] HMIntentHandler has been set to nil"
+ "[%{public}@] HomePod is not eligible for intent handling"
+ "[%{public}@] Intent: [ %@ ] is %@ successfully"
+ "[%{public}@] Invoking completion for intent %@ with response %@"
+ "[%{public}@] Passed-in outcome is invalid"
+ "[%{public}@] This intent contains unsecuring actions and needs user's authentication"
+ "[%{public}@] This intent contains unsecuring actions but the device does not enable the passcode"
+ "[%{public}@] Unlock required for intent: [ %@ ]"
- "%{public}@%@ time takes too long. Timer already fired"
- "%{public}@Execution is not allowed for intent: [ %@ ]"
- "%{public}@Failed to %@ intent: [ %@ ] - error %@"
- "%{public}@HMIntentHandler has been set to nil"
- "%{public}@HomePod is not eligible for intent handling"
- "%{public}@Intent: [ %@ ] is %@ successfully"
- "%{public}@Invoking completion for intent %@ with response %@"
- "%{public}@Passed-in outcome is invalid"
- "%{public}@This intent contains unsecuring actions and needs user's authentication"
- "%{public}@This intent contains unsecuring actions but the device does not enable the passcode"
- "%{public}@Unlock required for intent: [ %@ ]"

```
