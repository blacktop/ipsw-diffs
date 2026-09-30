## ProximityAppleIDSetup

> `/System/Library/PrivateFrameworks/ProximityAppleIDSetup.framework/ProximityAppleIDSetup`

```diff

-62.0.0.0.0
-  __TEXT.__text: 0x113b00
-  __TEXT.__auth_stubs: 0x1b70
-  __TEXT.__objc_methlist: 0x584
-  __TEXT.__const: 0xe148
-  __TEXT.__cstring: 0x50d0
-  __TEXT.__swift5_typeref: 0x3e2b
-  __TEXT.__oslogstring: 0x6051
-  __TEXT.__swift5_capture: 0xd0c
-  __TEXT.__constg_swiftt: 0x49f4
-  __TEXT.__swift5_reflstr: 0x2611
-  __TEXT.__swift5_fieldmd: 0x31c4
-  __TEXT.__swift5_builtin: 0x1cc
-  __TEXT.__swift5_assocty: 0x668
-  __TEXT.__swift5_proto: 0xd2c
-  __TEXT.__swift5_types: 0x3d0
+62.459.0.0.0
+  __TEXT.__text: 0x123d10
+  __TEXT.__auth_stubs: 0x1b80
+  __TEXT.__objc_methlist: 0x924
+  __TEXT.__const: 0xff58
+  __TEXT.__cstring: 0x50a0
+  __TEXT.__swift5_typeref: 0x3fef
+  __TEXT.__oslogstring: 0x6a81
+  __TEXT.__swift5_capture: 0xd44
+  __TEXT.__constg_swiftt: 0x4cbc
+  __TEXT.__swift5_reflstr: 0x2831
+  __TEXT.__swift5_fieldmd: 0x3388
+  __TEXT.__swift5_builtin: 0x1f4
+  __TEXT.__swift5_assocty: 0x680
+  __TEXT.__swift5_proto: 0xd7c
+  __TEXT.__swift5_types: 0x3f4
   __TEXT.__swift5_mpenum: 0x1c4
   __TEXT.__swift5_protos: 0x124
-  __TEXT.__unwind_info: 0x6118
-  __TEXT.__eh_frame: 0xdbbc
+  __TEXT.__swift_as_entry: 0x654
+  __TEXT.__swift_as_ret: 0x78c
+  __TEXT.__unwind_info: 0x6038
+  __TEXT.__eh_frame: 0xf04c
   __TEXT.__objc_classname: 0x68
-  __TEXT.__objc_methname: 0x170b
+  __TEXT.__objc_methname: 0x174f
   __TEXT.__objc_methtype: 0xa15
-  __DATA_CONST.__got: 0x520
-  __DATA_CONST.__const: 0x418
-  __DATA_CONST.__objc_classlist: 0x278
+  __DATA_CONST.__got: 0x538
+  __DATA_CONST.__const: 0x250
+  __DATA_CONST.__objc_classlist: 0x2b0
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x598
+  __DATA_CONST.__objc_selrefs: 0x728
   __DATA_CONST.__objc_protorefs: 0x48
-  __AUTH_CONST.__auth_got: 0xdb8
-  __AUTH_CONST.__auth_ptr: 0x928
-  __AUTH_CONST.__const: 0x8310
-  __AUTH_CONST.__objc_const: 0x9e60
-  __AUTH.__objc_data: 0x1b80
-  __AUTH.__data: 0x63a8
-  __DATA.__data: 0x4770
-  __DATA.__common: 0x1d8
-  __DATA.__bss: 0x183f0
+  __AUTH_CONST.__auth_got: 0xdc0
+  __AUTH_CONST.__auth_ptr: 0x9f0
+  __AUTH_CONST.__const: 0x8910
+  __AUTH_CONST.__objc_const: 0x9b28
+  __AUTH.__objc_data: 0x1b68
+  __AUTH.__data: 0x6bf8
+  __DATA.__data: 0x48a0
+  __DATA.__common: 0x128
+  __DATA.__bss: 0x18e20
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7156
-  Symbols:   371
-  CStrings:  1212
+  Functions: 7044
+  Symbols:   484
+  CStrings:  1256
 
Symbols:
+ _ACAccountTypeIdentifierAppleAccount
+ _OBJC_CLASS_$_ACAccountType
+ _OBJC_CLASS_$_AKProtoAccountContext
+ _object_getClass
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
- __swift_FORCE_LOAD_$_swiftFileProvider
- _swift_allocateGenericValueMetadata
- _swift_initStructMetadata
CStrings:
+ "Adding proto account context to bypass shielding"
+ "AgeAttestationPhase1"
+ "Attempting to get a partial account"
+ "AuthKit"
+ "PASAccountProtocol makeDefaultContext for feature .childSetup"
+ "PASAccountProtocol makeDefaultContext given target has proto account: %{bool}d"
+ "PASAccountProvider setTargetAccount %s with context: %{public}s"
+ "PASDeviceInfoExchanger buildPayload account.ageRange: %s"
+ "PASDeviceInfoExchanger buildPayload account.firstName: %s"
+ "PASDeviceInfoExchanger buildPayload account: %s"
+ "PASDeviceInfoExchanger buildPayload did not find primaryAppleAccount. Attempting to get partialAppleAccount"
+ "PASDeviceInfoExchanger saveRemoteDeviceData for prox type device: %s"
+ "PASDeviceInfoExchanger saveRemoteDeviceData recevied peer's account: %s"
+ "PASDeviceInfoExchanger saveRemoteDeviceData recevied peer's device: %s"
+ "PASDeviceInfoExchanger saveRemoteDeviceData target account.ageRange: %s"
+ "PASDeviceInfoExchanger saveRemoteDeviceData target account.firstName: %s"
+ "PASDeviceInfoExchanger saveRemoteDeviceData target account: %s"
+ "PASFlowStepConnectPeer prepareForPresentation has a partial account, skipping presentation"
+ "PASFlowStepConnectPeer prepareForPresentation targetAccount %{mask.hash}@ exists"
+ "PASFlowStepFamilyPicker continueWithSelectedAccount"
+ "PASFlowStepFamilyPicker createNewAccount"
+ "PASFlowStepFamilyPicker setFamilyMembers called"
+ "PASFlowStepFamilyPicker setFamilyMembers called again!"
+ "PASFlowStepProtoAccountPicker continueWithSelectedAccount"
+ "PASFlowStepProtoAccountPicker createNewAccount"
+ "PASFlowStepProtoAccountPicker fetchPresentables"
+ "PASFlowStepProtoAccountPicker fetchPresentables called again!"
+ "PASFlowStepProtoAccountPicker fetchPresentables failed with error %{public}@"
+ "PASFlowStepProtoAccountPicker fetchPresentables task was cancelled"
+ "PASFlowStepProtoAccountPicker nextStep has a localAccount which should not happen. Proceed with caution!"
+ "PASFlowStepProtoAccountPicker pickerSelection createAccount, setting Family Member context for family repair request"
+ "PASFlowStepSelectPicker nextStep is family picker"
+ "PASFlowStepSelectPicker nextStep is proto account picker"
+ "PASFlowStepSelectPicker nextStep no extension handle found"
+ "PASFlowStepSourceAuthentication updateTargetAccount shouldUpdateTargetAccount"
+ "PASFlowStepSourceAuthentication updateTargetAccount to %s"
+ "PASTargetFlowController ended before Start finished"
+ "PASTargetFlowController presenter is nil"
+ "PASTargetFlowController shutDown"
+ "ProximityAppleIDSetup.PASFlowStepProtoAccountPicker"
+ "SOURCE_ALL_SET_CONTEXT_SUBTITLE_"
+ "SOURCE_ALL_SET_CONTEXT_SUBTITLE_DEPENDENT"
+ "SOURCE_ALL_SET_CONTEXT_TITLE"
+ "We do not have the protoAccount method"
+ "We do not have the proto_ageRange method"
+ "We do not have the proto_givenName method"
+ "We have the protoAccount method, using it"
+ "We have the proto_ageRange method, using it"
+ "We have the proto_givenName method, using it"
+ "_TtC21ProximityAppleIDSetup15PASProtoAccount"
+ "_TtC21ProximityAppleIDSetup17PASAccountContext"
+ "_TtC21ProximityAppleIDSetup20PASPickerPresentable"
+ "_TtC21ProximityAppleIDSetup29PASFlowStepProtoAccountPicker"
+ "_TtC21ProximityAppleIDSetup34PASFlowStepTargetProtoAccountStart"
+ "_TtCC21ProximityAppleIDSetup17PASAccountContext12FamilyMember"
+ "_TtCC21ProximityAppleIDSetup17PASAccountContext15ExistingAccount"
+ "_TtCC21ProximityAppleIDSetup17PASAccountContext8Personal"
+ "_featureFlags"
+ "_presentables"
+ "_selectedPresentable"
+ "missingAccount"
+ "protoAccount"
+ "proto_ageRange"
+ "proto_givenName"
+ "setProtoAccountContext:"
- "Can't construct Array with count < 0"
- "Insufficient space allocated to copy string contents"
- "PASFlowStepFamilyPicker fetchFamilyMembers called again!"
- "PASFlowStepSelectPicker nextStep no extension handle found; falling back to family picker"
- "PASTargetFlowController presenter is nil in handleCancel"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_TtC21ProximityAppleIDSetup26PASFamilyMemberPresentable"
- "invalid Collection: less than 'count' elements in collection"

```
