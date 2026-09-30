## NFRadioPowerSwitch

> `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFRadioPowerSwitch.xpc/NFRadioPowerSwitch`

```diff

-363.10.0.0.0
-  __TEXT.__text: 0x1570
-  __TEXT.__auth_stubs: 0x2b0
+364.20.0.0.0
+  __TEXT.__text: 0x118c
+  __TEXT.__auth_stubs: 0x240
   __TEXT.__objc_stubs: 0x3a0
   __TEXT.__objc_methlist: 0x1a4
   __TEXT.__const: 0x70
   __TEXT.__objc_classname: 0x79
   __TEXT.__objc_methname: 0x3eb
   __TEXT.__objc_methtype: 0x15a
-  __TEXT.__cstring: 0x325
-  __TEXT.__oslogstring: 0x1d2
+  __TEXT.__cstring: 0x2ed
+  __TEXT.__oslogstring: 0x14b
   __TEXT.__unwind_info: 0x98
-  __DATA_CONST.__auth_got: 0x160
+  __DATA_CONST.__auth_got: 0x128
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0x90
   __DATA_CONST.__cfstring: 0x140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 004A8FE0-7110-3B97-B0EB-1B8B5EB4FCD0
+  UUID: 554FDA98-C788-3B52-8A5F-D5C40D6A5FDC
   Functions: 11
-  Symbols:   75
-  CStrings:  126
+  Symbols:   68
+  CStrings:  128
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _class_isMetaClass
- _objc_claimAutoreleasedReturnValue
- _objc_release_x28
- _objc_retain_x2
- _objc_retain_x3
- _object_getClass
- _object_getClassName
- _sel_getName
Functions:
~ sub_100000bc0 : 144 -> 148
~ sub_100000c50 -> sub_100000c54 : 148 -> 152
~ sub_100000cfc -> sub_100000d04 : 100 -> 104
~ sub_100000e5c -> sub_100000e68 : 216 -> 224
~ sub_10000106c -> sub_100001080 : 1604 -> 1092
~ sub_1000016b0 -> sub_1000014c4 : 2668 -> 2164
CStrings:
+ "%s:%i Available locs are  %@"
+ "%s:%i Couldn't create notification! %d"
+ "%s:%i Current loc is %@"
+ "%s:%i Failed to display radio status alert."
+ "%s:%i Failed to get bundle"
+ "%s:%i Failed to open URL"
+ "%s:%i Launching URL: %@"
+ "%s:%i No action taken"
+ "%s:%i Prefered loc is %@"
+ "%{public}s:%i Available locs are  %@"
+ "%{public}s:%i Couldn't create notification! %d"
+ "%{public}s:%i Current loc is %@"
+ "%{public}s:%i Failed to display radio status alert."
+ "%{public}s:%i Failed to get bundle"
+ "%{public}s:%i Failed to open URL"
+ "%{public}s:%i Launching URL: %@"
+ "%{public}s:%i No action taken"
+ "%{public}s:%i Prefered loc is %@"
+ "-[NFSettingsNotification _getLocalizedText:withBundle:]"
+ "-[NFSettingsNotification _requestUserNotificationWithCompletion:popupInterval:]"
+ "/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework"
- "%c[%{public}s %{public}s]:%i Available locs are  %@"
- "%c[%{public}s %{public}s]:%i Couldn't create notification! %d"
- "%c[%{public}s %{public}s]:%i Current loc is %@"
- "%c[%{public}s %{public}s]:%i Failed to display radio status alert."
- "%c[%{public}s %{public}s]:%i Failed to get bundle"
- "%c[%{public}s %{public}s]:%i Failed to open URL"
- "%c[%{public}s %{public}s]:%i Launching URL: %@"
- "%c[%{public}s %{public}s]:%i No action taken"
- "%c[%{public}s %{public}s]:%i Prefered loc is %@"
- "/System/Library/PrivateFrameworks/NearField.framework"

```
