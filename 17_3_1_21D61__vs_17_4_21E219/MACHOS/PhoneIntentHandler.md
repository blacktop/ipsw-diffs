## PhoneIntentHandler

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/PlugIns/PhoneIntentHandler.appex/PhoneIntentHandler`

```diff

-1431.400.41.2.1
-  __TEXT.__text: 0x2e85c
-  __TEXT.__auth_stubs: 0xd00
-  __TEXT.__objc_stubs: 0x4f00
-  __TEXT.__objc_methlist: 0x17b0
-  __TEXT.__cstring: 0x156f
-  __TEXT.__oslogstring: 0x67ed
-  __TEXT.__objc_classname: 0x642
-  __TEXT.__objc_methname: 0x64c4
-  __TEXT.__objc_methtype: 0x118e
-  __TEXT.__const: 0x130
+1431.500.151.2.9
+  __TEXT.__text: 0x2f4ac
+  __TEXT.__auth_stubs: 0xd60
+  __TEXT.__objc_stubs: 0x5000
+  __TEXT.__objc_methlist: 0x1830
+  __TEXT.__cstring: 0x183f
+  __TEXT.__oslogstring: 0x6a5f
+  __TEXT.__objc_classname: 0x687
+  __TEXT.__objc_methname: 0x67ea
+  __TEXT.__objc_methtype: 0x129d
+  __TEXT.__const: 0x120
   __TEXT.__gcc_except_tab: 0x1e8
   __TEXT.__swift5_typeref: 0x2b8
   __TEXT.__swift5_fieldmd: 0x8c

   __TEXT.__swift5_reflstr: 0x39
   __TEXT.__swift5_capture: 0x1a4
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x1280
-  __TEXT.__eh_frame: 0x988
-  __DATA_CONST.__auth_got: 0x690
+  __TEXT.__unwind_info: 0x12ac
+  __TEXT.__eh_frame: 0x9a0
+  __DATA_CONST.__auth_got: 0x6c0
   __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0xb08
-  __DATA_CONST.__cfstring: 0xf20
-  __DATA_CONST.__objc_classlist: 0x150
+  __DATA_CONST.__const: 0xb70
+  __DATA_CONST.__cfstring: 0xf40
+  __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0xd8
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x400
+  __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x1d0
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x5048
-  __DATA.__objc_selrefs: 0x15e8
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x3f0
-  __DATA.__objc_superrefs: 0xc0
-  __DATA.__objc_ivar: 0x16c
-  __DATA.__objc_data: 0xf58
-  __DATA.__data: 0xb80
+  __DATA.__objc_const: 0x5390
+  __DATA.__objc_selrefs: 0x1638
+  __DATA.__objc_ivar: 0x17c
+  __DATA.__objc_data: 0xfa8
+  __DATA.__data: 0xc40
   __DATA.__bss: 0x58
   __DATA.__common: 0x20
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 775
-  Symbols:   397
-  CStrings:  1788
+  Functions: 792
+  Symbols:   403
+  CStrings:  1842
 
Symbols:
+ _OBJC_CLASS_$_EmergencyServicesOverrideProvider
+ _OBJC_CLASS_$_TULabeledHandle
+ _OBJC_METACLASS_$_EmergencyServicesOverrideProvider
+ _TUShouldUseSuperboxTelephonyProvider
+ __TUIsInternalInstall
+ _swift_initStaticObject
CStrings:
+ "\f"
+ "\x14"
+ "#EmergencyServicesOverrideProvider found %lu handles in emergencyServicesOverride. Transforming them to TULabeledHandle."
+ "#StartCallIntentHandler emergencyServicesOverrideEnabled==true and emergencyProvider shared %lu emergencyLabeledHandles. Using those."
+ "#StartCallIntentHandler emergencyServicesOverrideEnabled==true and emergencyProvider.emergencyLabeledHandles is empty. Checking override."
+ "#StartCallIntentHandler not internal build or emergency services override disabled. Using handles from emergency provider."
+ "@\"<IntentHandlerFeatureFlags>\""
+ "@\"EmergencyServicesOverrideProvider\""
+ "@\"EmergencyServicesOverrideProvider\"16@0:8"
+ "@\"TUCallProvider\""
+ "@\"TUCallProvider\"16@0:8"
+ "@48@0:8@\"NSObject<OS_dispatch_queue>\"16@\"IntentHandlerFeatureFlags\"24@\"TUCallProvider\"32@\"EmergencyServicesOverrideProvider\"40"
+ "@?<B@?>16@0:8"
+ "B8@?0"
+ "EmergencyServicesOverrideProvider"
+ "EmergencyServicesOverrideProviding"
+ "Insufficient space allocated to copy string contents"
+ "Siri.PhoneIntentHandler.EmergencyServicesOverride"
+ "SiriPhone/emergencyServicesOverrideEnabled AND isInternalBuild: %{public}@"
+ "Superbox is enabled, returning YES"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"<IntentHandlerFeatureFlags>\",&,N,V_featureFlags"
+ "T@\"EmergencyServicesOverrideProvider\",R,N"
+ "T@\"EmergencyServicesOverrideProvider\",R,N,V_emergencyServicesOverrideProvider"
+ "T@\"NSArray\",R,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"TUCallProvider\",R,N"
+ "T@\"TUCallProvider\",R,N,V_emergencyProvider"
+ "T@?,C,N"
+ "T@?,C,N,V_isSuperboxEnabled"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "_emergencyProvider"
+ "_emergencyServicesOverrideProvider"
+ "_isSuperboxEnabled"
+ "dictionaryForKey:"
+ "emergencyServicesOverrideEnabled"
+ "emergencyServicesOverrideProvider"
+ "emergencyServicesOverrides"
+ "initWithDialIntent:providerManager:contactsDataSource:senderIdentityClient:isEmergencyServicesOverrideEnabled:"
+ "initWithDispatchQueue:featureFlags:"
+ "initWithDispatchQueue:featureFlags:emergencyProvider:emergencyServicesOverrideProvider:"
+ "initWithHandle:label:isSuggested:"
+ "invalid Collection: less than 'count' elements in collection"
+ "isSuperboxEnabled"
+ "setIsSuperboxEnabled:"
+ "siriEmergencyServices"
+ "v24@0:8@?<B@?>16"
+ "v32@?0@8@16^B24"
- "\t"
- "\x13"
- "@24@0:8@\"NSObject<OS_dispatch_queue>\"16"
- "initWithDispatchQueue:"

```
