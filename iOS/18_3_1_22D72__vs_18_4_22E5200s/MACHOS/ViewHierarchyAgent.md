## ViewHierarchyAgent

> `/usr/libexec/ViewHierarchyAgent`

```diff

 71.0.0.0.0
-  __TEXT.__text: 0x1530c
-  __TEXT.__auth_stubs: 0xa30
-  __TEXT.__const: 0x2e4
-  __TEXT.__cstring: 0x725
+  __TEXT.__text: 0x15b80
+  __TEXT.__auth_stubs: 0xa50
+  __TEXT.__const: 0x304
+  __TEXT.__cstring: 0xa9b
   __TEXT.__swift5_typeref: 0x250
   __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__constg_swiftt: 0x13c

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x14
+  __TEXT.__swift_as_entry: 0x24
+  __TEXT.__swift_as_ret: 0x28
   __TEXT.__oslogstring: 0x23e
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x420
+  __TEXT.__unwind_info: 0x418
   __TEXT.__eh_frame: 0x2c8
-  __DATA_CONST.__auth_got: 0x518
-  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__auth_got: 0x528
+  __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x118
   __DATA_CONST.__const: 0xae8
   __DATA_CONST.__objc_classlist: 0x18

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 363
-  Symbols:   736
-  CStrings:  73
+  Functions: 369
+  Symbols:   762
+  CStrings:  90
 
Symbols:
+ _$s18ViewHierarchyAgent17CaptureControllerC15requestExecutor33_D209E654CA4122E0E152E9E22B079C70LLAA07RequestG0_pvg
+ _$s18ViewHierarchyAgent17CaptureControllerC18temporaryDirectory33_D209E654CA4122E0E152E9E22B079C70LL10Foundation3URLVvg
+ _$s18ViewHierarchyAgent24SystemXPCRequestExecutorC10connection7Mercury17XPCPeerConnection_pvg
+ _$s18ViewHierarchyAgentAAC14remoteListener33_C8D45B17DDDED33F12A416B68754945ALL7Mercury21XPCListenerConnection_pvg
+ _$s18ViewHierarchyAgentAAC14systemListener33_C8D45B17DDDED33F12A416B68754945ALL7Mercury21XPCListenerConnection_pvg
+ _$s18ViewHierarchyAgentAAC17targetHubListener33_C8D45B17DDDED33F12A416B68754945ALL7Mercury21XPCListenerConnection_pvg
+ _$s18ViewHierarchyAgentAAC18captureControllers33_C8D45B17DDDED33F12A416B68754945ALLSDys5Int32VAA17CaptureControllerCGvg
+ _$s18ViewHierarchyAgentAAC18captureControllers33_C8D45B17DDDED33F12A416B68754945ALLSDys5Int32VAA17CaptureControllerCGvs
+ _$s18ViewHierarchyAgentAAC18pendingConnections33_C8D45B17DDDED33F12A416B68754945ALLSDys5Int32VScCy7Mercury23SystemXPCPeerConnectionCs5Error_pGGvg
+ _$s18ViewHierarchyAgentAAC18pendingConnections33_C8D45B17DDDED33F12A416B68754945ALLSDys5Int32VScCy7Mercury23SystemXPCPeerConnectionCs5Error_pGGvs
+ _$s18ViewHierarchyAgentAAC19remoteListenerQueue33_C8D45B17DDDED33F12A416B68754945ALLSo17OS_dispatch_queueCvg
+ _$s18ViewHierarchyAgentAAC19systemListenerQueue33_C8D45B17DDDED33F12A416B68754945ALLSo17OS_dispatch_queueCvg
+ _$s18ViewHierarchyAgentAAC22targetHubListenerQueue33_C8D45B17DDDED33F12A416B68754945ALLSo17OS_dispatch_queueCvg
+ _$s18ViewHierarchyAgentAAC6sharedABvgZ
+ _$sSS8UTF8ViewV13_foreignIndex5afterSS0D0VAF_tF
+ _$sSS8UTF8ViewV13_foreignIndex_8offsetBySS0D0VAF_SitF
+ _$sSS8UTF8ViewV17_foreignSubscript8positions5UInt8VSS5IndexV_tF
+ _$sSS9UTF16ViewV5index_8offsetBySS5IndexVAF_SitF
+ _$sSa22_allocateUninitializedySayxG_SpyxGtSiFZSo17OS_dispatch_queueC8DispatchE10AttributesV_Tt0gq5
+ _$sSv16initializeMemory2as4from5countSpyxGxm_SPyxGSitlFs5UInt8V_Ttgq5
+ _$ss11_StringGutsV27_slowEnsureMatchingEncodingySS5IndexVAEF
+ _$ss15ContiguousArrayVAByxGycfCs5UInt8V_Ttgq5
+ _$ss22_ContiguousArrayBufferV19_uninitializedCount15minimumCapacityAByxGSi_SitcfCs5UInt8V_Tt1gq5
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _type_layout_string 18ViewHierarchyAgent0aB7RequestO
- _$s18ViewHierarchyAgent0aB7RequestOwCP
- _$s18ViewHierarchyAgent0aB7RequestOwca
- _$s18ViewHierarchyAgent0aB7RequestOwcp
- _$s18ViewHierarchyAgent0aB7RequestOwta
- _$s18ViewHierarchyAgent0aB7RequestOwxx
- _$sSa22_allocateUninitializedySayxG_SpyxGtSiFZSo17OS_dispatch_queueC8DispatchE10AttributesV_Tgmq5
- _$sSv16initializeMemory2as4from5countSpyxGxm_SPyxGSitlFs5UInt8V_Tgmq5
- _$ss15ContiguousArrayVAByxGycfCs5UInt8V_Tgmq5
- _$ss22_ContiguousArrayBufferV19_uninitializedCount15minimumCapacityAByxGSi_SitcfCs5UInt8V_Tgmq5
CStrings:
+ "Insufficient space allocated to copy string contents"
+ "String index is out of bounds"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawBufferPointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawBufferPointer with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "UnsafeMutableRawPointer.initializeMemory with negative count"
+ "UnsafeRawBufferPointer with negative count"
+ "invalid Collection: less than 'count' elements in collection"
+ "invalid Collection: more than 'count' elements in collection"

```
