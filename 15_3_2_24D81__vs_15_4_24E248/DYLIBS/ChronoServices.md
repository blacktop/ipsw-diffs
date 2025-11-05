## ChronoServices

> `/System/Library/PrivateFrameworks/ChronoServices.framework/Versions/A/ChronoServices`

```diff

-537.4.1.0.0
-  __TEXT.__text: 0xddd48
-  __TEXT.__auth_stubs: 0x2660
-  __TEXT.__objc_methlist: 0x6724
-  __TEXT.__const: 0x52ec
-  __TEXT.__gcc_except_tab: 0xa3e4
-  __TEXT.__cstring: 0x5f05
-  __TEXT.__oslogstring: 0x40ce
+537.5.41.0.0
+  __TEXT.__text: 0xe3b34
+  __TEXT.__auth_stubs: 0x26b0
+  __TEXT.__objc_methlist: 0x710c
+  __TEXT.__const: 0x544c
+  __TEXT.__gcc_except_tab: 0xa4c4
+  __TEXT.__cstring: 0x5e85
+  __TEXT.__oslogstring: 0x429a
   __TEXT.__dlopen_cstrs: 0x5c
-  __TEXT.__swift5_typeref: 0x1df4
-  __TEXT.__swift5_capture: 0x974
-  __TEXT.__swift5_reflstr: 0x104a
+  __TEXT.__swift5_typeref: 0x1f2e
+  __TEXT.__swift5_capture: 0x984
+  __TEXT.__swift5_reflstr: 0x10da
   __TEXT.__swift5_assocty: 0x448
-  __TEXT.__constg_swiftt: 0x1da0
-  __TEXT.__swift5_fieldmd: 0x10b4
+  __TEXT.__constg_swiftt: 0x204c
+  __TEXT.__swift5_fieldmd: 0x11c4
   __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_proto: 0x410
-  __TEXT.__swift5_types: 0x1c0
+  __TEXT.__swift5_proto: 0x418
+  __TEXT.__swift5_types: 0x1d0
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__swift5_protos: 0x34
-  __TEXT.__unwind_info: 0x60a0
-  __TEXT.__eh_frame: 0x2f30
+  __TEXT.__swift_as_entry: 0x50
+  __TEXT.__swift_as_ret: 0x50
+  __TEXT.__swift5_protos: 0x44
+  __TEXT.__unwind_info: 0x5f58
+  __TEXT.__eh_frame: 0x3040
   __TEXT.__objc_classname: 0x129d
-  __TEXT.__objc_methname: 0xc627
-  __TEXT.__objc_methtype: 0x211a
-  __TEXT.__objc_stubs: 0x5c00
-  __DATA_CONST.__got: 0x9a8
-  __DATA_CONST.__const: 0x5f8
-  __DATA_CONST.__objc_classlist: 0x548
+  __TEXT.__objc_methname: 0xc7e6
+  __TEXT.__objc_methtype: 0x215d
+  __TEXT.__objc_stubs: 0x5c60
+  __DATA_CONST.__got: 0x9c8
+  __DATA_CONST.__const: 0x610
+  __DATA_CONST.__objc_classlist: 0x568
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a08
+  __DATA_CONST.__objc_selrefs: 0x2ac8
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x2e0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1348
-  __AUTH_CONST.__const: 0x5da8
-  __AUTH_CONST.__cfstring: 0x4140
-  __AUTH_CONST.__objc_const: 0x1d050
+  __AUTH_CONST.__auth_got: 0x1370
+  __AUTH_CONST.__const: 0x5e00
+  __AUTH_CONST.__cfstring: 0x41e0
+  __AUTH_CONST.__objc_const: 0x1c320
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH.__objc_data: 0x31c8
-  __AUTH.__data: 0x1b48
-  __DATA.__objc_ivar: 0x680
-  __DATA.__data: 0x2730
+  __AUTH.__objc_data: 0x3600
+  __AUTH.__data: 0x1c00
+  __DATA.__objc_ivar: 0x684
+  __DATA.__data: 0x27d8
   __DATA.__bss: 0x7da0
-  __DATA.__common: 0x1a0
+  __DATA.__common: 0x1b8
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 56DD3067-691C-3DA0-BC95-2267A9356975
-  Functions: 6138
-  Symbols:   8606
-  CStrings:  4290
+  UUID: A9BF4397-67D4-365C-A667-E0D85DA1B64A
+  Functions: 6178
+  Symbols:   8709
+  CStrings:  4313
 
Symbols:
+ +[CHSChronoServicesConnection ncBridgeConnection].cold.1
+ +[CHSChronoServicesConnection sharedInstance].cold.1
+ +[CHSIntentReference _encodeToOPACK:error:].cold.1
+ +[CHSIntentReference referenceFromIntent:error:]
+ +[CHSToolServiceConnection sharedInstance].cold.1
+ -[CHSConfiguredWidgetDescriptor _initWithUniqueIdentifier:widget:metrics:displayProperties:fallbackToDefaultDisplayIfNecessary:]
+ -[CHSIntentReference _initWithGenericIntent:schemaData:error:]
+ -[CHSIntentReference _initWithGenericIntent:schemaData:error:].cold.1
+ -[CHSIntentReference _initWithGenericIntent:schemaData:error:].cold.2
+ -[CHSWidget initWithExtensionIdentity:kind:family:intent:activityIdentifier:personaIdentifier:]
+ -[CHSWidget initWithExtensionIdentity:kind:family:intentReference:activityIdentifier:personaIdentifier:]
+ -[CHSWidget initWithExtensionIdentity:kind:family:intentReference:activityIdentifier:personaIdentifier:].cold.1
+ -[CHSWidget personaIdentifier]
+ -[CHSWidget widgetByRemovingPersona]
+ -[CHSWidgetDescriptorProvider initWithConnection:extensionProvider:providerOptions:].cold.1
+ -[CHSWidgetExtensionProvider initWithConnection:providerOptions:eduProvider:].cold.1
+ CHSLogChronoServices.cold.1
+ CHSLogClientSnapshots.cold.1
+ CHSLogSubscriptions.cold.1
+ CHSLogWidgetHosts.cold.1
+ GCC_except_table360
+ GCC_except_table373
+ GCC_except_table383
+ GCC_except_table393
+ GCC_except_table403
+ OBJC_IVAR_$_CHSWidget._personaIdentifier
+ _CHSSystemVersionStringToCompareAgainstFromSDKAndPlatform.cold.2
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$__TtC14ChronoServices16StateCaptureItem
+ _OBJC_CLASS_$__TtC14ChronoServices17StateCaptureEntry
+ _OBJC_CLASS_$__TtC14ChronoServices19StateCaptureService
+ _OBJC_CLASS_$__TtC14ChronoServices23StateCaptureInvalidator
+ _OBJC_METACLASS_$__TtC14ChronoServices16StateCaptureItem
+ _OBJC_METACLASS_$__TtC14ChronoServices17StateCaptureEntry
+ _OBJC_METACLASS_$__TtC14ChronoServices19StateCaptureService
+ _OBJC_METACLASS_$__TtC14ChronoServices23StateCaptureInvalidator
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ __21-[CHSWidget isEqual:]_block_invoke.35
+ __21-[CHSWidget isEqual:]_block_invoke.39
+ __21-[CHSWidget isEqual:]_block_invoke.43
+ __DATA__TtC14ChronoServices16StateCaptureItem
+ __DATA__TtC14ChronoServices17StateCaptureEntry
+ __DATA__TtC14ChronoServices19StateCaptureService
+ __DATA__TtC14ChronoServices23StateCaptureInvalidator
+ __INSTANCE_METHODS__TtC14ChronoServices16StateCaptureItem
+ __INSTANCE_METHODS__TtC14ChronoServices17StateCaptureEntry
+ __INSTANCE_METHODS__TtC14ChronoServices19StateCaptureService
+ __INSTANCE_METHODS__TtC14ChronoServices23StateCaptureInvalidator
+ __IVARS__TtC14ChronoServices16StateCaptureItem
+ __IVARS__TtC14ChronoServices17StateCaptureEntry
+ __IVARS__TtC14ChronoServices19StateCaptureService
+ __IVARS__TtC14ChronoServices23StateCaptureInvalidator
+ __METACLASS_DATA__TtC14ChronoServices16StateCaptureItem
+ __METACLASS_DATA__TtC14ChronoServices17StateCaptureEntry
+ __METACLASS_DATA__TtC14ChronoServices19StateCaptureService
+ __METACLASS_DATA__TtC14ChronoServices23StateCaptureInvalidator
+ __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIvEENS_9allocatorIS5_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt9type_infoeqB8ne190102ERKS_
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__110__function12__value_funcIFN5apple4aiml12flatbuffers26OffsetIvEEmEED2B8ne190102Ev
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIvEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__125__throw_bad_function_callB8ne190102Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIvEENS_9allocatorIS5_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIvEENS_9allocatorIS5_EEEC2B8ne190102Em
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___21-[CHSWidget isEqual:]_block_invoke_3
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_project_boxed_opaque_existential_1Tm
+ __plistableTypes.cold.1
+ _calloc
+ _objc_msgSend$_initWithGenericIntent:schemaData:error:
+ _objc_msgSend$_initWithUniqueIdentifier:widget:metrics:displayProperties:fallbackToDefaultDisplayIfNecessary:
+ _objc_msgSend$initWithExtensionIdentity:kind:family:intent:activityIdentifier:personaIdentifier:
+ _objc_msgSend$initWithExtensionIdentity:kind:family:intentReference:activityIdentifier:personaIdentifier:
+ _objc_msgSend$personaIdentifier
+ _os_state_add_handler
+ _os_state_remove_handler
+ _strlcpy
+ _symbolic $s14ChronoServices14StateCapturingP
+ _symbolic $s14ChronoServices20StateCaptureManagingP
+ _symbolic $s14ChronoServices23StateHierarchyCapturingP
+ _symbolic $s14ChronoServices25StateCaptureInvalidatableP
+ _symbolic SDySSSaySSGG
+ _symbolic SDySS_____G 14ChronoServices16StateCaptureItemC
+ _symbolic Sccy___________pG 10Foundation4DataV s5ErrorP
+ _symbolic _____ 14ChronoServices16StateCaptureItemC
+ _symbolic _____ 14ChronoServices17StateCaptureEntryC
+ _symbolic _____ 14ChronoServices19StateCaptureServiceC
+ _symbolic _____ 14ChronoServices23StateCaptureInvalidatorC
+ _symbolic ______p 14ChronoServices14StateCapturingP
+ _symbolic ______pSg 14ChronoServices25StateCaptureInvalidatableP
+ _symbolic _____ySSSaySSGG s18_DictionaryStorageC
+ _symbolic _____ySS_____G s18_DictionaryStorageC 14ChronoServices16StateCaptureItemC
+ _symbolic _____y__________G s18_DictionaryStorageC s6UInt64V 14ChronoServices17StateCaptureEntryC
+ _symbolic ypIegr_
+ _symbolic ypyc
+ block_copy_helper.113
+ block_copy_helper.119
+ block_copy_helper.128
+ block_copy_helper.131
+ block_copy_helper.137
+ block_copy_helper.140
+ block_copy_helper.146
+ block_copy_helper.152
+ block_copy_helper.188
+ block_copy_helper.194
+ block_copy_helper.200
+ block_copy_helper.206
+ block_copy_helper.212
+ block_copy_helper.218
+ block_copy_helper.224
+ block_copy_helper.230
+ block_copy_helper.236
+ block_copy_helper.242
+ block_copy_helper.248
+ block_copy_helper.254
+ block_copy_helper.260
+ block_copy_helper.266
+ block_copy_helper.272
+ block_copy_helper.278
+ block_copy_helper.284
+ block_copy_helper.290
+ block_copy_helper.296
+ block_copy_helper.302
+ block_copy_helper.308
+ block_copy_helper.314
+ block_copy_helper.320
+ block_copy_helper.326
+ block_copy_helper.332
+ block_copy_helper.338
+ block_copy_helper.345
+ block_descriptor.115
+ block_descriptor.121
+ block_descriptor.130
+ block_descriptor.133
+ block_descriptor.139
+ block_descriptor.142
+ block_descriptor.148
+ block_descriptor.154
+ block_descriptor.190
+ block_descriptor.196
+ block_descriptor.202
+ block_descriptor.208
+ block_descriptor.214
+ block_descriptor.220
+ block_descriptor.226
+ block_descriptor.232
+ block_descriptor.238
+ block_descriptor.244
+ block_descriptor.250
+ block_descriptor.256
+ block_descriptor.262
+ block_descriptor.268
+ block_descriptor.274
+ block_descriptor.280
+ block_descriptor.286
+ block_descriptor.292
+ block_descriptor.298
+ block_descriptor.304
+ block_descriptor.310
+ block_descriptor.316
+ block_descriptor.322
+ block_descriptor.328
+ block_descriptor.334
+ block_descriptor.340
+ block_descriptor.347
+ block_destroy_helper.114
+ block_destroy_helper.120
+ block_destroy_helper.129
+ block_destroy_helper.132
+ block_destroy_helper.138
+ block_destroy_helper.141
+ block_destroy_helper.147
+ block_destroy_helper.153
+ block_destroy_helper.189
+ block_destroy_helper.195
+ block_destroy_helper.201
+ block_destroy_helper.207
+ block_destroy_helper.213
+ block_destroy_helper.219
+ block_destroy_helper.225
+ block_destroy_helper.231
+ block_destroy_helper.237
+ block_destroy_helper.243
+ block_destroy_helper.249
+ block_destroy_helper.255
+ block_destroy_helper.261
+ block_destroy_helper.267
+ block_destroy_helper.273
+ block_destroy_helper.279
+ block_destroy_helper.285
+ block_destroy_helper.291
+ block_destroy_helper.297
+ block_destroy_helper.303
+ block_destroy_helper.309
+ block_destroy_helper.315
+ block_destroy_helper.321
+ block_destroy_helper.327
+ block_destroy_helper.333
+ block_destroy_helper.339
+ block_destroy_helper.346
+ keypath_set.82Tm
+ objectdestroy.150Tm
+ objectdestroy.198Tm
+ objectdestroy.204Tm
+ objectdestroy.210Tm
+ objectdestroy.300Tm
- -[CHSIntentReference _initWithGenericIntent:schemaData:]
- -[CHSIntentReference _initWithGenericIntent:schemaData:].cold.1
- -[CHSIntentReference _initWithGenericIntent:schemaData:].cold.2
- -[CHSWidget initWithExtensionIdentity:kind:family:intentReference:activityIdentifier:].cold.1
- GCC_except_table362
- GCC_except_table375
- GCC_except_table385
- GCC_except_table395
- GCC_except_table405
- __21-[CHSWidget isEqual:]_block_invoke.32
- __21-[CHSWidget isEqual:]_block_invoke.36
- __21-[CHSWidget isEqual:]_block_invoke.40
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIvEENS_9allocatorIS5_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt9exception4whatEv
- __ZNKSt9type_infoeqB8ne180100ERKS_
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__110__function12__value_funcIFN5apple4aiml12flatbuffers26OffsetIvEEmEED2B8ne180100Ev
- __ZNSt3__117bad_function_callD0Ev
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIvEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__125__throw_bad_function_callB8ne180100Ev
- __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIvEENS_9allocatorIS5_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIvEENS_9allocatorIS5_EEEC2Em
- __ZNSt9exceptionD2Ev
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- __ZTSNSt3__117bad_function_callE
- __intentDataFromIntent
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_ChronoServices
- _intentDataFromIntent.cold.1
- _keypath_setTm
- _objc_msgSend$_initWithGenericIntent:schemaData:
- _objc_msgSend$initWithExtensionIdentity:kind:family:intentReference:activityIdentifier:
- _objectdestroyTm
- _symbolic _____Sg So6CGRectV
- block_copy_helper.117
- block_copy_helper.126
- block_copy_helper.129
- block_copy_helper.135
- block_copy_helper.138
- block_copy_helper.144
- block_copy_helper.150
- block_copy_helper.186
- block_copy_helper.192
- block_copy_helper.198
- block_copy_helper.204
- block_copy_helper.210
- block_copy_helper.216
- block_copy_helper.222
- block_copy_helper.228
- block_copy_helper.234
- block_copy_helper.240
- block_copy_helper.246
- block_copy_helper.252
- block_copy_helper.258
- block_copy_helper.264
- block_copy_helper.270
- block_copy_helper.276
- block_copy_helper.282
- block_copy_helper.288
- block_copy_helper.294
- block_copy_helper.300
- block_copy_helper.306
- block_copy_helper.312
- block_copy_helper.318
- block_copy_helper.324
- block_copy_helper.330
- block_copy_helper.336
- block_copy_helper.343
- block_copy_helper.40
- block_descriptor.119
- block_descriptor.128
- block_descriptor.131
- block_descriptor.137
- block_descriptor.140
- block_descriptor.146
- block_descriptor.152
- block_descriptor.188
- block_descriptor.194
- block_descriptor.200
- block_descriptor.206
- block_descriptor.212
- block_descriptor.218
- block_descriptor.224
- block_descriptor.230
- block_descriptor.236
- block_descriptor.242
- block_descriptor.248
- block_descriptor.254
- block_descriptor.260
- block_descriptor.266
- block_descriptor.272
- block_descriptor.278
- block_descriptor.284
- block_descriptor.290
- block_descriptor.296
- block_descriptor.302
- block_descriptor.308
- block_descriptor.314
- block_descriptor.320
- block_descriptor.326
- block_descriptor.332
- block_descriptor.338
- block_descriptor.345
- block_descriptor.42
- block_destroy_helper.118
- block_destroy_helper.127
- block_destroy_helper.130
- block_destroy_helper.136
- block_destroy_helper.139
- block_destroy_helper.145
- block_destroy_helper.151
- block_destroy_helper.187
- block_destroy_helper.193
- block_destroy_helper.199
- block_destroy_helper.205
- block_destroy_helper.211
- block_destroy_helper.217
- block_destroy_helper.223
- block_destroy_helper.229
- block_destroy_helper.235
- block_destroy_helper.241
- block_destroy_helper.247
- block_destroy_helper.253
- block_destroy_helper.259
- block_destroy_helper.265
- block_destroy_helper.271
- block_destroy_helper.277
- block_destroy_helper.283
- block_destroy_helper.289
- block_destroy_helper.295
- block_destroy_helper.301
- block_destroy_helper.307
- block_destroy_helper.313
- block_destroy_helper.319
- block_destroy_helper.325
- block_destroy_helper.331
- block_destroy_helper.337
- block_destroy_helper.344
- block_destroy_helper.41
- objectdestroy.148Tm
- objectdestroy.196Tm
- objectdestroy.202Tm
- objectdestroy.208Tm
- objectdestroy.298Tm
CStrings:
+ "%@[%@:%@:%@:%@%@:%@~%@]"
+ "@40@0:8@16@24^@32"
+ "@52@0:8@16@24@32@40B48"
+ "@64@0:8@16@24q32@40@48@56"
+ "ChronoServices.StateCaptureEntry"
+ "ChronoServices.StateCaptureInvalidator"
+ "ChronoServices.StateCaptureItem"
+ "Could not OPACK encode backing store dictionary: %@"
+ "Could not OPACK encode intent: %@"
+ "No `INCodable` backing store found for intent of type: %@: %@"
+ "T@\"NSString\",R,C,N,V_personaIdentifier"
+ "[state-capture] StateCaptureEntry created with title: %{public}s"
+ "[state-capture] added StateCaptureItem with title: %{public}s, identifier: %{public}s"
+ "[state-capture][%s] cannot allocate memory for state data"
+ "[state-capture][%s] cannot capture state data larger than 32KB"
+ "[state-capture][%s] cannot encode state data into a plist: %{public}@"
+ "[state-capture][%s] os_state_add_handler() failed to return a handle"
+ "^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8"
+ "_TtC14ChronoServices16StateCaptureItem"
+ "_TtC14ChronoServices17StateCaptureEntry"
+ "_TtC14ChronoServices19StateCaptureService"
+ "_TtC14ChronoServices23StateCaptureInvalidator"
+ "_initWithGenericIntent:schemaData:error:"
+ "_initWithUniqueIdentifier:widget:metrics:displayProperties:fallbackToDefaultDisplayIfNecessary:"
+ "_personaIdentifier"
+ "captureHandler"
+ "carPlayHomeScreen"
+ "com.apple.chrono.stateCaptureService"
+ "dataWithPropertyList:format:options:error:"
+ "initWithExtensionIdentity:kind:family:intent:activityIdentifier:personaIdentifier:"
+ "initWithExtensionIdentity:kind:family:intentReference:activityIdentifier:personaIdentifier:"
+ "invalidatable"
+ "invalidated"
+ "itemsByIdentifier"
+ "personaIdentifier"
+ "referenceFromIntent:error:"
+ "subitemsByIdentifier"
+ "title"
+ "widgetByRemovingPersona"
- "%@[%@:%@:%@:%@%@:%@]"
- "Can't construct Array with count < 0"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_initWithGenericIntent:schemaData:"
- "invalid Collection: less than 'count' elements in collection"

```
