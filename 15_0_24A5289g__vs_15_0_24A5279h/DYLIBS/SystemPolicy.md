## SystemPolicy

> `/System/Library/PrivateFrameworks/SystemPolicy.framework/Versions/A/SystemPolicy`

```diff

-620.0.16.0.0
-  __TEXT.__text: 0x16be0
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_methlist: 0x11d0
+620.0.7.0.0
+  __TEXT.__text: 0x15e90
+  __TEXT.__auth_stubs: 0x7c0
+  __TEXT.__objc_methlist: 0x1048
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x1556
+  __TEXT.__cstring: 0x14e4
   __TEXT.__gcc_except_tab: 0xf8
-  __TEXT.__oslogstring: 0x1226
-  __TEXT.__unwind_info: 0x698
-  __TEXT.__objc_classname: 0x27c
-  __TEXT.__objc_methname: 0x36b7
-  __TEXT.__objc_methtype: 0xa97
-  __TEXT.__objc_stubs: 0x21c0
-  __DATA_CONST.__got: 0x2a8
+  __TEXT.__oslogstring: 0x119e
+  __TEXT.__unwind_info: 0x660
+  __TEXT.__objc_classname: 0x259
+  __TEXT.__objc_methname: 0x3545
+  __TEXT.__objc_methtype: 0xa77
+  __TEXT.__objc_stubs: 0x1f60
+  __DATA_CONST.__got: 0x280
   __DATA_CONST.__const: 0x150
-  __DATA_CONST.__objc_classlist: 0xe0
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd18
+  __DATA_CONST.__objc_selrefs: 0xca0
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x478
-  __AUTH_CONST.__auth_got: 0x3f8
+  __AUTH_CONST.__auth_got: 0x3f0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x830
-  __AUTH_CONST.__cfstring: 0x20a0
-  __AUTH_CONST.__objc_const: 0x32b8
+  __AUTH_CONST.__cfstring: 0x2020
+  __AUTH_CONST.__objc_const: 0x2f68
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x224
+  __AUTH.__objc_data: 0x820
+  __DATA.__objc_ivar: 0x1fc
   __DATA.__data: 0x248
   __DATA.__bss: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 664
-  Symbols:   1635
-  CStrings:  297
+  Functions: 628
+  Symbols:   1551
+  CStrings:  293
 
Symbols:
+ __block_literal_global.63
+ __block_literal_global.84
+ __block_literal_global.86
+ __block_literal_global.88
- -[ProvenanceEntry .cxx_destruct]
- -[ProvenanceEntry attributes]
- -[ProvenanceEntry bundleID]
- -[ProvenanceEntry cdhash]
- -[ProvenanceEntry createMetadata]
- -[ProvenanceEntry description]
- -[ProvenanceEntry flags]
- -[ProvenanceEntry redactedDescription]
- -[ProvenanceEntry rootID]
- -[ProvenanceEntry setBundleID:]
- -[ProvenanceEntry setCdhash:]
- -[ProvenanceEntry setFlags:]
- -[ProvenanceEntry setRootID:]
- -[ProvenanceEntry setSigningID:]
- -[ProvenanceEntry setTeamID:]
- -[ProvenanceEntry setUniqueID:]
- -[ProvenanceEntry setUrl:]
- -[ProvenanceEntry signingID]
- -[ProvenanceEntry teamID]
- -[ProvenanceEntry uniqueID]
- -[ProvenanceEntry url]
- -[SPExecutionPolicy allowGatekeeperPolicy:error:]
- -[SPProvenanceTracking getProvenanceIDForURL:]
- -[TrackingAttributes description]
- -[TrackingAttributes flags]
- -[TrackingAttributes identifier]
- -[TrackingAttributes initWithData:]
- -[TrackingAttributes redactedDescription]
- -[TrackingAttributes serialize]
- -[TrackingAttributes setFlags:]
- -[TrackingAttributes setIdentifier:]
- OBJC_IVAR_$_ProvenanceEntry.bundleID
- OBJC_IVAR_$_ProvenanceEntry.cdhash
- OBJC_IVAR_$_ProvenanceEntry.flags
- OBJC_IVAR_$_ProvenanceEntry.rootID
- OBJC_IVAR_$_ProvenanceEntry.signingID
- OBJC_IVAR_$_ProvenanceEntry.teamID
- OBJC_IVAR_$_ProvenanceEntry.uniqueID
- OBJC_IVAR_$_ProvenanceEntry.url
- OBJC_IVAR_$_TrackingAttributes.flags
- OBJC_IVAR_$_TrackingAttributes.identifier
- _NSURLIsSystemImmutableKey
- _NSURLIsUserImmutableKey
- _OBJC_CLASS_$_ProvenanceEntry
- _OBJC_CLASS_$_TrackingAttributes
- _OBJC_METACLASS_$_ProvenanceEntry
- _OBJC_METACLASS_$_TrackingAttributes
- __OBJC_$_INSTANCE_METHODS_ProvenanceEntry
- __OBJC_$_INSTANCE_METHODS_TrackingAttributes
- __OBJC_$_INSTANCE_VARIABLES_ProvenanceEntry
- __OBJC_$_INSTANCE_VARIABLES_TrackingAttributes
- __OBJC_$_PROP_LIST_ProvenanceEntry
- __OBJC_$_PROP_LIST_TrackingAttributes
- __OBJC_CLASS_RO_$_ProvenanceEntry
- __OBJC_CLASS_RO_$_TrackingAttributes
- __OBJC_METACLASS_RO_$_ProvenanceEntry
- __OBJC_METACLASS_RO_$_TrackingAttributes
- ___49-[SPExecutionPolicy allowGatekeeperPolicy:error:]_block_invoke
- ___kCFBooleanFalse
- ___kCFBooleanTrue
- __block_literal_global.64
- _doWithoutImmutability
- _getXattrData
- _getxattr
- _objc_msgSend$allowGatekeeperPolicy:withReply:
- _objc_msgSend$dataWithBytesNoCopy:length:freeWhenDone:
- _objc_msgSend$flags
- _objc_msgSend$identifier
- _objc_msgSend$initWithData:
- _objc_msgSend$rootID
- _objc_msgSend$setBundleID:
- _objc_msgSend$setCdhash:
- _objc_msgSend$setFlags:
- _objc_msgSend$setIdentifier:
- _objc_msgSend$setResourceValue:forKey:error:
- _objc_msgSend$setRootID:
- _objc_msgSend$setSigningID:
- _objc_msgSend$setTeamID:
- _objc_msgSend$setUniqueID:
- _objc_msgSend$setUrl:
- _objc_msgSend$uniqueID
- _objc_msgSend$unsignedLongLongValue
- _objc_msgSend$unsignedShortValue
- getXattrData.cold.1
- getXattrData.cold.2
CStrings:
- "PE - %!@(MISSING), %!@(MISSING), self: (%!l(MISSING)lx), parent: (%!l(MISSING)lx)"
- "PE - %!@(MISSING), self: (%!l(MISSING)lx), parent: (%!l(MISSING)lx)"
- "TA(%!l(MISSING)lx, %!x(MISSING))"
- "com.apple.provenance"

```
