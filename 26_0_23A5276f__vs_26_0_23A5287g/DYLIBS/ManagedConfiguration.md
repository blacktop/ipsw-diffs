## ManagedConfiguration

> `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration`

```diff

-2422.0.0.0.0
-  __TEXT.__text: 0xf7f84
+2424.0.0.0.0
+  __TEXT.__text: 0xf842c
   __TEXT.__auth_stubs: 0x1750
-  __TEXT.__objc_methlist: 0xb154
-  __TEXT.__const: 0x1394
-  __TEXT.__cstring: 0x17c93
-  __TEXT.__oslogstring: 0x8cc9
+  __TEXT.__objc_methlist: 0xb164
+  __TEXT.__const: 0x13a4
+  __TEXT.__cstring: 0x17cc3
+  __TEXT.__oslogstring: 0x8f7c
   __TEXT.__gcc_except_tab: 0x10c4
   __TEXT.__ustring: 0x50
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x3080
+  __TEXT.__unwind_info: 0x3118
   __TEXT.__objc_classname: 0xc99
-  __TEXT.__objc_methname: 0x1e028
-  __TEXT.__objc_methtype: 0x236c
+  __TEXT.__objc_methname: 0x1e05c
+  __TEXT.__objc_methtype: 0x236f
   __TEXT.__objc_stubs: 0xdb60
   __DATA_CONST.__got: 0xa88
-  __DATA_CONST.__const: 0x4d28
+  __DATA_CONST.__const: 0x4d30
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5ca0
+  __DATA_CONST.__objc_selrefs: 0x5ca8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0xbb8
   __AUTH_CONST.__const: 0x2070
-  __AUTH_CONST.__cfstring: 0x19240
+  __AUTH_CONST.__cfstring: 0x192a0
   __AUTH_CONST.__objc_const: 0xd6a8
-  __AUTH_CONST.__objc_intobj: 0x408
+  __AUTH_CONST.__objc_intobj: 0x420
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x1220
   __DATA.__objc_ivar: 0x980

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E958E463-BD39-3F7E-8217-684030BB6638
-  Functions: 5620
-  Symbols:   17327
-  CStrings:  12197
+  UUID: 1C8A2F94-FCCA-39A4-9426-E6D0AC2903E8
+  Functions: 5627
+  Symbols:   17336
+  CStrings:  12209
 
Symbols:
+ -[MCPasscodeManager unlockScreenTypeWithPublicPasscodeDict:isRecovery:deviceHandle:]
+ -[MCPasscodeManager unlockSimplePasscodeTypeWithPublicPasscodeDict:isRecovery:deviceHandle:]
+ -[MCProfileConnection(Misc) areSoftwareUpdatesAllowed]
+ GCC_except_table281
+ GCC_except_table7
+ _MCFeatureSoftwareUpdatesAllowed
+ _MCKeybagClearMementoBlobForHandle
+ _MCKeybagCurrentMaximumFailedPasscodeAttemptsForHandle
+ _MCKeybagCurrentPasscodeGenerationForHandle
+ _MCKeybagMementoBlobExistsForHandle
+ _MCKeybagMementoPasscodeGenerationForHandle
+ _MCKeybagMementoSupportedForHandle
+ _MCKeybagMementoSupportedForHandle.supported
+ _objc_msgSend$unlockScreenTypeWithPublicPasscodeDict:isRecovery:deviceHandle:
+ _objc_msgSend$unlockSimplePasscodeTypeWithPublicPasscodeDict:isRecovery:deviceHandle:
- -[MCPasscodeManager unlockScreenTypeWithPublicPasscodeDict:isRecovery:]
- -[MCPasscodeManager unlockSimplePasscodeTypeWithPublicPasscodeDict:isRecovery:]
- GCC_except_table280
- _MCKeybagMementoSupported.supported
- _objc_msgSend$unlockScreenTypeWithPublicPasscodeDict:isRecovery:
- _objc_msgSend$unlockSimplePasscodeTypeWithPublicPasscodeDict:isRecovery:
CStrings:
+ "DeviceHandle"
+ "Full Keyboard"
+ "No passcode generation provided to filter characteristics. Returning nil"
+ "No passcode generation provided to filter public dictionary. Returning nil"
+ "Unable to retrieve unlock screen type for generation %{public}@, defaulting to %{public}@. Public Dictionary Exists: %{public}@. Is Empty: %{public}@. Generation Exists: %{public}@. Is Recovery: %{public}@"
+ "Unable to retrieve unlock simple type for generation %{public}@, but retrieved simple unlock screen. Defaulting to Simple 4 Digits"
+ "Unable to retrieve unlock simple type for generation %{public}@, defaulting to Not Simple. Public Dictionary Exists: %{public}@. Is Empty: %{public}@. Generation Exists: %{public}@. Is Recovery: %{public}@"
+ "allowSoftwareUpdates"
+ "areSoftwareUpdatesAllowed"
+ "i36@0:8@16B24@28"
+ "unlockScreenTypeWithPublicPasscodeDict:isRecovery:deviceHandle:"
+ "unlockSimplePasscodeTypeWithPublicPasscodeDict:isRecovery:deviceHandle:"
- "i28@0:8@16B24"
- "unlockScreenTypeWithPublicPasscodeDict:isRecovery:"
- "unlockSimplePasscodeTypeWithPublicPasscodeDict:isRecovery:"

```
