## amfid

> `/usr/libexec/amfid`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-1171.0.3.0.0
-  __TEXT.__text: 0x1eda8
-  __TEXT.__auth_stubs: 0x11e0
-  __TEXT.__objc_stubs: 0x1040
+1171.0.12.0.0
+  __TEXT.__text: 0x153a4
+  __TEXT.__auth_stubs: 0x1140
+  __TEXT.__objc_stubs: 0x860
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x5f4
-  __TEXT.__const: 0xb14
+  __TEXT.__objc_methlist: 0x344
+  __TEXT.__const: 0xa6c
   __TEXT.__swift5_typeref: 0x49b
-  __TEXT.__cstring: 0x1bf2
+  __TEXT.__cstring: 0x11e9
   __TEXT.__swift5_reflstr: 0x175
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__constg_swiftt: 0x28c
   __TEXT.__swift5_fieldmd: 0x1b0
-  __TEXT.__objc_classname: 0xeb
-  __TEXT.__objc_methname: 0x1292
+  __TEXT.__objc_classname: 0x9e
+  __TEXT.__objc_methname: 0x9e7
   __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x18
   __TEXT.__oslogstring: 0x1129
-  __TEXT.__objc_methtype: 0x432
+  __TEXT.__objc_methtype: 0x31d
   __TEXT.__swift5_capture: 0x1c
   __TEXT.__gcc_except_tab: 0x36c
-  __TEXT.__unwind_info: 0x698
+  __TEXT.__unwind_info: 0x5c8
   __TEXT.__eh_frame: 0x3d0
-  __DATA_CONST.__const: 0xa18
-  __DATA_CONST.__cfstring: 0xa00
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__const: 0x948
+  __DATA_CONST.__cfstring: 0x240
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x908
-  __DATA_CONST.__got: 0x2d8
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__auth_got: 0x8b8
+  __DATA_CONST.__got: 0x2b0
   __DATA_CONST.__auth_ptr: 0x1e8
-  __DATA.__objc_const: 0x9c0
-  __DATA.__objc_selrefs: 0x548
-  __DATA.__objc_ivar: 0x34
-  __DATA.__objc_data: 0x310
+  __DATA.__objc_const: 0x5e0
+  __DATA.__objc_selrefs: 0x330
+  __DATA.__objc_ivar: 0x8
+  __DATA.__objc_data: 0x220
   __DATA.__data: 0x648
   __DATA.__bss: 0x8a8
   __DATA.__common: 0x50

   - /System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/Versions/A/AppleMobileFileIntegrity
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libCoreEntitlements.dylib
+  - /usr/lib/libDetachedCertificates.dylib
+  - /usr/lib/libDetachedCertificatesLookup.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 467
-  Symbols:   469
-  CStrings:  584
+  Functions: 369
+  Symbols:   450
+  CStrings:  411
 
Symbols:
+ _OBJC_CLASS_$_DetachedCertificatesLookup
+ _os_lockdown_mode_enabled
- _NSLocalizedDescriptionKey
- _OBJC_CLASS_$_NSArray
- _OBJC_CLASS_$_NSError
- _OBJC_CLASS_$_NSMutableArray
- _OBJC_CLASS_$_NSMutableDictionary
- _ccder_blob_decode_bitstring
- _ccder_blob_decode_tag
- _ccder_blob_decode_tl
- _ccder_blob_decode_uint64
- _ccder_encode_constructed_tl
- _ccder_encode_raw_octet_string
- _ccder_encode_uint64
- _ccder_sizeof
- _ccder_sizeof_raw_octet_string
- _ccder_sizeof_uint64
- _ccsha1_di
- _ccsha224_di
- _ccsha256_di
- _ccsha384_di
- _ccsha512_di
- _objc_autorelease
CStrings:
+ "com.apple.amfi.developer_mode_state"
+ "developer_app_executions"
+ "developer_mode_state"
+ "lockdown_mode_state"
+ "numberWithBool:"
- "&"
- "*40@0:8@16*24*32"
- "/System/Library/Security/DetachedCertificates.der"
- "/System/Library/Security/PQCCertificates.der"
- "@\"NSData\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@24@0:8^@16"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24^@32"
- "B32@0:8@16^@24"
- "B40@0:8@16@24^@32"
- "B40@0:8^{?=*Q}16^@24^@32"
- "B40@0:8^{?=Q{?=*Q}}16^@24^@32"
- "B48@0:8@16@24@32^@40"
- "CTGetAKIDFromCertificate failed for %@: %d"
- "CTGetSKIDFromCertificate failed for %@: %d"
- "Compatibility version mismatch: self=%llu, other=%llu"
- "DetachedCertificateEntry"
- "DetachedCertificates.der"
- "DetachedCertificatesFile"
- "DetachedCertificatesLookup"
- "DetachedCertificatesLookupErrorDomain"
- "Error draining certificate entry fields"
- "Error iterating sequence: %d"
- "Expected INTEGER for compatibility_version, tag=0x%llx"
- "Expected INTEGER for version, tag=0x%llx"
- "Expected OCTET STRING for certificate"
- "Expected OCTET STRING for skid"
- "Expected SEQUENCE for certificate entry, got 0x%llx"
- "Expected SEQUENCE for certificate list"
- "Expected [0] EXPLICIT tag, got 0x%llx"
- "Expected [1] EXPLICIT tag, got 0x%llx"
- "Failed to allocate encoding buffer"
- "Failed to decode akid"
- "Failed to decode certificate"
- "Failed to decode certificate sequence: %d"
- "Failed to decode root DER: %d"
- "Failed to decode skid"
- "Failed to encode [0] EXPLICIT tag"
- "Failed to encode [1] EXPLICIT tag"
- "Failed to encode [2] EXPLICIT tag"
- "Failed to encode compatibility_version"
- "Failed to encode intermediate certificate entry"
- "Failed to encode intermediate certificates SEQUENCE"
- "Failed to encode leaf certificate entry"
- "Failed to encode leaf certificates SEQUENCE"
- "Failed to encode root SEQUENCE"
- "Failed to encode root certificate entry"
- "Failed to encode root certificates SEQUENCE"
- "Failed to encode version"
- "Failed to extract SKID from CMS blob: %d"
- "Failed to get compatibility_version element"
- "Failed to get intermediate certificates element"
- "Failed to get leaf certificates element"
- "Failed to get version element"
- "Failed to parse compatibility_version integer"
- "Failed to parse version integer"
- "Failed to write to path: %@"
- "File does not exist at path: %@"
- "Intermediate AKID does not match root SKID for leaf at index %lu"
- "Intermediate certificate's AKID does not match root certificate's SKID"
- "Invalid parameters: executablePath and cmsData are required"
- "Invalid parameters: executablePath and skid are required"
- "Leaf AKID does not match intermediate SKID for leaf at index %lu"
- "Leaf certificate does not have an AKID"
- "Leaf certificate's AKID does not match intermediate certificate's SKID"
- "No detached certificates found for executable: %@"
- "No intermediate certificate found for leaf at index %lu"
- "No intermediate certificate found matching leaf's AKID"
- "No leaf certificate found with the specified SKID"
- "Q"
- "Q24@0:8@16"
- "Root element is not a SEQUENCE, tag=0x%llx"
- "System/Library/Security/DetachedCertificates.der"
- "T@\"NSData\",R,N,V_akid"
- "T@\"NSData\",R,N,V_certificate"
- "T@\"NSData\",R,N,V_skid"
- "T@\"NSMutableArray\",&,N,V_intermediateCertificates"
- "T@\"NSMutableArray\",&,N,V_leafCertificates"
- "T@\"NSMutableArray\",&,N,V_rootCertificates"
- "T@\"NSMutableDictionary\",&,N,V_intermediateSKIDMap"
- "T@\"NSMutableDictionary\",&,N,V_leafSKIDMap"
- "T@\"NSMutableDictionary\",&,N,V_rootSKIDMap"
- "TQ,N,V_compatibilityVersion"
- "TQ,N,V_version"
- "Unsupported compatibility_version: %llu (max supported: 1)"
- "_akid"
- "_certificate"
- "_compatibilityVersion"
- "_intermediateCertificates"
- "_intermediateSKIDMap"
- "_leafCertificates"
- "_leafSKIDMap"
- "_rootCertificates"
- "_rootSKIDMap"
- "_skid"
- "_version"
- "addCertificateChainWithLeaf:intermediate:error:"
- "addCertificateChainWithLeaf:intermediate:root:error:"
- "addCertificateChainsWithLeaves:parents:error:"
- "addObject:"
- "addObjectsFromArray:"
- "akid"
- "array"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "certificate"
- "com.apple.security.DetachedCertificates"
- "compatibilityVersion"
- "copy"
- "dataWithBytes:length:"
- "dataWithContentsOfFile:options:error:"
- "derEncodedSize"
- "dictionary"
- "dictionaryWithCapacity:"
- "encodeCertificateEntry:der:der_end:"
- "errorWithDomain:code:userInfo:"
- "extractAKIDFromCertificate:certificateName:error:"
- "extractSKIDFromCMSData:error:"
- "extractSKIDFromCertificate:certificateName:error:"
- "initWithSKID:certificate:akid:"
- "intermediate"
- "intermediate of leaf at index %lu"
- "intermediateCertificates"
- "intermediateSKIDMap"
- "isEqualToArray:"
- "isEqualToData:"
- "leaf"
- "leaf at index %lu"
- "leafCertificates"
- "leafSKIDMap"
- "loadCertificatesFileMatching:skid:"
- "loadFromPath:error:"
- "lookupCertificateChainForSKID:error:"
- "lookupCertificatesForExecutable:skid:error:"
- "lookupDetachedCertificatesFileForExecutable:cmsData:error:"
- "lookupDetachedCertificatesFileForExecutable:skid:error:"
- "mergeWithFile:error:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "parent"
- "parseCertificateEntry:certificate:error:"
- "parseCertificateSequence:certificates:error:"
- "parseFromData:error:"
- "q24@?0@\"DetachedCertificateEntry\"8@\"DetachedCertificateEntry\"16"
- "rebuildSKIDMaps"
- "removeAllObjects"
- "removeRootCertificates"
- "root"
- "root of leaf at index %lu"
- "rootCertificates"
- "rootSKIDMap"
- "searchInsideOutForFile:skid:"
- "setCompatibilityVersion:"
- "setIntermediateCertificates:"
- "setIntermediateSKIDMap:"
- "setLeafCertificates:"
- "setLeafSKIDMap:"
- "setObject:forKeyedSubscript:"
- "setRootCertificates:"
- "setRootSKIDMap:"
- "setVersion:"
- "sizeOfCertificateEntry:"
- "skid"
- "sortCertificateArrays"
- "sortUsingComparator:"
- "stringByAppendingPathComponent:"
- "stringByDeletingLastPathComponent"
- "stringByResolvingSymlinksInPath"
- "stringWithFormat:"
- "v24@0:8Q16"
- "version"
- "writeToData:"
- "writeToFile:options:error:"
- "writeToPath:error:"
```
