## amfid

> `/usr/libexec/amfid`

```diff

-938.80.6.0.0
-  __TEXT.__text: 0x197b8
-  __TEXT.__auth_stubs: 0x14f0
+938.100.76.0.1
+  __TEXT.__text: 0x19220
+  __TEXT.__auth_stubs: 0x14c0
   __TEXT.__objc_stubs: 0xc40
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x194
-  __TEXT.__const: 0xaef
+  __TEXT.__objc_methlist: 0x35c
+  __TEXT.__const: 0xb2f
   __TEXT.__gcc_except_tab: 0x4fc
-  __TEXT.__oslogstring: 0x1492
-  __TEXT.__cstring: 0x1980
+  __TEXT.__oslogstring: 0x1562
+  __TEXT.__cstring: 0x1743
   __TEXT.__objc_classname: 0x57
   __TEXT.__objc_methname: 0xb69
   __TEXT.__objc_methtype: 0x2fd
   __TEXT.__swift5_typeref: 0x461
-  __TEXT.__swift5_reflstr: 0x155
+  __TEXT.__swift5_reflstr: 0x175
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__constg_swiftt: 0x284
-  __TEXT.__swift5_fieldmd: 0x1a4
+  __TEXT.__swift5_fieldmd: 0x1b0
   __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_capture: 0x1c
-  __TEXT.__unwind_info: 0x750
+  __TEXT.__unwind_info: 0x730
   __TEXT.__eh_frame: 0x3d0
-  __DATA_CONST.__auth_got: 0xa90
+  __DATA_CONST.__auth_got: 0xa78
   __DATA_CONST.__got: 0x368
   __DATA_CONST.__auth_ptr: 0x1d8
   __DATA_CONST.__const: 0xa60

   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x930
-  __DATA.__objc_selrefs: 0x398
+  __DATA.__objc_const: 0x5e0
+  __DATA.__objc_selrefs: 0x430
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x220
   __DATA.__data: 0x630

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 531
-  Symbols:   530
-  CStrings:  542
+  Functions: 523
+  Symbols:   532
+  CStrings:  535
 
Symbols:
+ _os_variant_allows_internal_security_policies
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initializeBufferWithCopyOfBuffer
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
CStrings:
+ "[migration] %@: failed creating auxiliary signature: %@"
+ "[migration] %s: copy profile error: %u"
+ "[migration] %s: created auxiliary signature"
+ "[migration] %s: missing Team ID"
+ "[migration] %s: upgraded auxiliary signature"
+ "[migration] SEP epoch: %u"
+ "[migration] code-signing: %u | %u"
+ "[migration] demo mode not required"
+ "[migration] demo mode: %u | %u | %u"
+ "[migration] initiating MIS"
+ "[migration] initiating demo mode"
+ "[migration] initiating provisioning profiles"
+ "[migration] provisioning profiles not required | epoch"
+ "[migration] provisioning profiles not required | monitor"
+ "[migration] using internal build"
+ "__provisioningProfilesMigrate_block_invoke"
+ "initiating SEP init-state ratcheting: %u"
- "%@: failed creating auxiliary signature: %@"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "__misMigrate_block_invoke"
- "initiating AMFI migration | TXM: %u"
- "initiating MIS migration"
- "initiating SEP init-state ratcheting"
- "initiating demo state migration: %u | %u | %u"
- "invalid Collection: less than 'count' elements in collection"
- "misMigrate | %s: copy profile error: %u"
- "misMigrate | %s: created auxiliary signature"
- "misMigrate | %s: missing Team ID"
- "misMigrate | %s: upgraded auxiliary signature"
- "skipping AMFI migration: %u"
- "skipping auxiliary signatures for non-TXM system"

```
