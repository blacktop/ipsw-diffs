## amfid

> `/usr/libexec/amfid`

```diff

-938.81.1.0.0
-  __TEXT.__text: 0x165f8
-  __TEXT.__auth_stubs: 0x11a0
-  __TEXT.__objc_stubs: 0x6e0
+938.101.1.0.0
+  __TEXT.__text: 0x16230
+  __TEXT.__auth_stubs: 0x1170
+  __TEXT.__objc_stubs: 0x700
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x194
-  __TEXT.__const: 0x91f
-  __TEXT.__oslogstring: 0xf42
-  __TEXT.__cstring: 0x1450
+  __TEXT.__objc_methlist: 0x35c
+  __TEXT.__const: 0x93f
+  __TEXT.__oslogstring: 0x1022
+  __TEXT.__cstring: 0x1233
   __TEXT.__gcc_except_tab: 0x35c
   __TEXT.__objc_classname: 0x57
-  __TEXT.__objc_methname: 0x801
+  __TEXT.__objc_methname: 0x80b
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
-  __TEXT.__unwind_info: 0x6d8
+  __TEXT.__unwind_info: 0x6c0
   __TEXT.__eh_frame: 0x3d0
-  __DATA_CONST.__auth_got: 0x8e8
+  __DATA_CONST.__auth_got: 0x8d0
   __DATA_CONST.__got: 0x288
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x848
+  __DATA_CONST.__const: 0x870
   __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x930
-  __DATA.__objc_selrefs: 0x240
+  __DATA.__objc_const: 0x5e0
+  __DATA.__objc_selrefs: 0x2e0
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x220
-  __DATA.__data: 0x668
+  __DATA.__data: 0x678
   __DATA.__bss: 0x838
   __DATA.__common: 0xc0
   __RESTRICT.__restrict: 0x0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: FE1FF53F-E465-39A5-80D9-4F1FB801CD98
-  Functions: 498
-  Symbols:   449
-  CStrings:  407
+  UUID: 568CF4DF-7451-3BB7-BB5A-5123E7EEA123
+  Functions: 496
+  Symbols:   446
+  CStrings:  404
 
Symbols:
+ _os_variant_allows_internal_security_policies
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
CStrings:
+ "23050"
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
+ "com.apple.dt.Xcode"
+ "profileID"
+ "selected profile: %{public}@ | %u"
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
- "initiating demo state migration: %u | %u | %u"
- "invalid Collection: less than 'count' elements in collection"
- "misMigrate | %s: copy profile error: %u"
- "misMigrate | %s: created auxiliary signature"
- "misMigrate | %s: missing Team ID"
- "misMigrate | %s: upgraded auxiliary signature"
- "skipping AMFI migration: %u"
- "skipping auxiliary signatures for non-TXM system"

```
