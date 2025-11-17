## BiometricKitUI

> `/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`

```diff

-661.0.0.0.0
-  __TEXT.__text: 0x5ec54
+661.2.1.0.0
+  __TEXT.__text: 0x5f75c
   __TEXT.__auth_stubs: 0xe20
-  __TEXT.__objc_methlist: 0x6a60
+  __TEXT.__objc_methlist: 0x6ae0
   __TEXT.__const: 0x9a4
   __TEXT.__gcc_except_tab: 0xe68
-  __TEXT.__cstring: 0x2dd6
-  __TEXT.__oslogstring: 0x43b8
+  __TEXT.__cstring: 0x2e26
+  __TEXT.__oslogstring: 0x46f4
   __TEXT.__dlopen_cstrs: 0x292
   __TEXT.__swift5_typeref: 0x96
   __TEXT.__swift5_capture: 0x34

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x1758
-  __TEXT.__objc_classname: 0xc86
-  __TEXT.__objc_methname: 0x129ac
+  __TEXT.__unwind_info: 0x1778
+  __TEXT.__objc_classname: 0xc88
+  __TEXT.__objc_methname: 0x12be3
   __TEXT.__objc_methtype: 0x3146
-  __TEXT.__objc_stubs: 0xd1e0
-  __DATA_CONST.__got: 0x800
-  __DATA_CONST.__const: 0x11d8
+  __TEXT.__objc_stubs: 0xd360
+  __DATA_CONST.__got: 0x820
+  __DATA_CONST.__const: 0x11e8
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4468
+  __DATA_CONST.__objc_selrefs: 0x44e0
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x188
   __AUTH_CONST.__auth_got: 0x728
   __AUTH_CONST.__const: 0x2f0
-  __AUTH_CONST.__cfstring: 0x30c0
-  __AUTH_CONST.__objc_const: 0xe718
+  __AUTH_CONST.__cfstring: 0x3100
+  __AUTH_CONST.__objc_const: 0xe778
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_floatobj: 0x80
-  __AUTH_CONST.__objc_intobj: 0x228
+  __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1060
   __AUTH.__data: 0xe0
-  __DATA.__objc_ivar: 0x978
+  __DATA.__objc_ivar: 0x980
   __DATA.__data: 0x1018
   __DATA.__bss: 0x2f0
   __DATA.__common: 0x200

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: AA0D7B2D-3565-3E2E-AD03-2C24CC83277F
-  Functions: 2446
-  Symbols:   8551
-  CStrings:  4909
+  UUID: EF3F830F-21DA-3798-8E90-E581E7B37F13
+  Functions: 2465
+  Symbols:   8609
+  CStrings:  4945
 
Symbols:
+ +[BiometricKitUI setOfActiveRestrictionUUIDs:]
+ -[BKUIDevice .cxx_destruct]
+ -[BKUIDevice deviceForType:]
+ -[BKUIDevice deviceForType:].cold.1
+ -[BKUIDevice deviceTypeForIdentityType:]
+ -[BKUIDevice deviceTypeForIdentityType:].cold.1
+ -[BKUIDevice identitiesForIdentityType:]
+ -[BKUIDevice identitiesForIdentityType:].cold.1
+ -[BKUIDevice init].cold.1
+ -[BKUIDevice init].cold.2
+ -[BKUIDevice init].cold.3
+ -[BKUIDevice isEnrolledInFaceID]
+ -[BKUIDevice pearlDevice]
+ -[BKUIDevice setPearlDevice:]
+ -[BKUIDevice setTouchIDDevice:]
+ -[BKUIDevice touchIDDevice]
+ -[BKUIPearlEnrollViewController setClientRestrictionOnPasscodeGracePeriod:]
+ -[BKUIPearlEnrollViewController setClientRestrictionOnPasscodeGracePeriod:].cold.1
+ GCC_except_table40
+ GCC_except_table49
+ _BKUIManagedConfigurationClientType
+ _BKUIManagedConfigurationFaceIDRestrictionsUUID
+ _MCFeaturePasscodeLockGraceTime
+ _OBJC_CLASS_$_BKDevicePearl
+ _OBJC_CLASS_$_BKDeviceTouchID
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_IVAR_$_BKUIDevice._pearlDevice
+ _OBJC_IVAR_$_BKUIDevice._touchIDDevice
+ ___89-[BKUIPearlEnrollViewController enrollOperation:finishedWithIdentity:animateImmediately:]_block_invoke.194
+ ___block_literal_global.198
+ _objc_msgSend$MCSetValueRestriction:value:
+ _objc_msgSend$applyRestrictionDictionary:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:
+ _objc_msgSend$clientRestrictionsForClientUUID:
+ _objc_msgSend$deviceForType:
+ _objc_msgSend$deviceTypeForIdentityType:
+ _objc_msgSend$identitiesForIdentityType:
+ _objc_msgSend$isEnrolledInFaceID
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$pearlDevice
+ _objc_msgSend$set
+ _objc_msgSend$setClientRestrictionOnPasscodeGracePeriod:
+ _objc_msgSend$touchIDDevice
- GCC_except_table39
- GCC_except_table48
- GCC_except_table59
- ___89-[BKUIPearlEnrollViewController enrollOperation:finishedWithIdentity:animateImmediately:]_block_invoke.192
- ___block_literal_global.196
CStrings:
+ "BKUIDevice setup: An error occured retrieving `BKDeviceTouchID`: %@"
+ "BKUIDevice setup: An error occured retrieving `BKPearlDevice`: %@"
+ "BKUIDevice setup: Unknown `BKDeviceType`: %ld"
+ "Did set client restriction on passcode grace period"
+ "Enrolled in Face ID: %@"
+ "Failed to set client restriction on passcode grace period"
+ "MCSetValueRestriction:value:"
+ "Skipping setting client restriction on passcode grace period as enrollment failed"
+ "Skipping setting client restriction on passcode grace period as it is currently already enforced"
+ "T@\"BKDevicePearl\",&,N,V_pearlDevice"
+ "T@\"BKDeviceTouchID\",&,N,V_touchIDDevice"
+ "Will check if we are enrolled in Face ID"
+ "Will set client restriction on passcode grace period"
+ "_pearlDevice"
+ "_touchIDDevice"
+ "applyRestrictionDictionary:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:"
+ "clientRestrictionsForClientUUID:"
+ "com.apple.BiometricKitUI"
+ "com.apple.BiometricsKitUI.FaceID.Restrictions"
+ "deviceForType:"
+ "deviceForType: Trying to find unknown `BKDevice` of type: %ld"
+ "deviceTypeForIdentityType:"
+ "deviceTypeForIdentityType: Trying to find unknown `BKIdentityType`of type: %ld"
+ "identitiesForIdentityType:"
+ "identitiesForIdentityType: Error occured when retrieving identities from `BKDevice` of type: %ld %@"
+ "isEnrolledInFaceID"
+ "isEqualToNumber:"
+ "pearlDevice"
+ "set"
+ "setClientRestrictionOnPasscodeGracePeriod:"
+ "setOfActiveRestrictionUUIDs:"
+ "setPearlDevice:"
+ "setTouchIDDevice:"
+ "touchIDDevice"

```
