## CoreRoutine

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine`

```diff

-1048.0.0.0.0
-  __TEXT.__text: 0x62974
+1053.0.1.0.0
+  __TEXT.__text: 0x62d94
   __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_methlist: 0x7d6c
+  __TEXT.__objc_methlist: 0x7d9c
   __TEXT.__const: 0x2b8
   __TEXT.__oslogstring: 0x3226
-  __TEXT.__cstring: 0x63ca
+  __TEXT.__cstring: 0x641e
   __TEXT.__gcc_except_tab: 0x36c
-  __TEXT.__unwind_info: 0x1de0
+  __TEXT.__unwind_info: 0x1e30
   __TEXT.__objc_classname: 0xf9a
-  __TEXT.__objc_methname: 0xec12
+  __TEXT.__objc_methname: 0xed14
   __TEXT.__objc_methtype: 0x26d0
-  __TEXT.__objc_stubs: 0x7480
+  __TEXT.__objc_stubs: 0x74c0
   __DATA_CONST.__got: 0x4a0
   __DATA_CONST.__const: 0x11a0
   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2838
+  __DATA_CONST.__objc_selrefs: 0x2858
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x428
   __DATA_CONST.__objc_arraydata: 0x98
   __AUTH_CONST.__auth_got: 0x348
   __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x5920
-  __AUTH_CONST.__objc_const: 0xe180
+  __AUTH_CONST.__cfstring: 0x5960
+  __AUTH_CONST.__objc_const: 0xe1e0
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x14a0
-  __DATA.__objc_ivar: 0x800
+  __DATA.__objc_ivar: 0x808
   __DATA.__data: 0x308
   __DATA_DIRTY.__objc_ivar: 0x12c
   __DATA_DIRTY.__objc_data: 0x16d0

   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3A22D609-4322-3BD1-B92F-E85FDBF8A478
-  Functions: 2804
-  Symbols:   8745
-  CStrings:  4405
+  UUID: B4FEFA3E-4C9A-3E7A-9C75-7E324C59BD89
+  Functions: 2808
+  Symbols:   8757
+  CStrings:  4417
 
Symbols:
+ +[NSDate(RTExtensions) getEarliestDate:]
+ -[RTUserCuration initWithIdentifier:submissionDate:expirationDate:entryDate:exitDate:visitIdentifier:originalLabel:curatedLabel:]
+ -[RTUserCuration originalLabel]
+ -[RTUserCuration visitIdentifier]
+ _OBJC_IVAR_$_RTUserCuration._originalLabel
+ _OBJC_IVAR_$_RTUserCuration._visitIdentifier
+ _objc_msgSend$initWithIdentifier:submissionDate:expirationDate:entryDate:exitDate:visitIdentifier:originalLabel:curatedLabel:
+ _objc_msgSend$originalLabel
+ _objc_msgSend$visitIdentifier
- _objc_msgSend$initWithIdentifier:submissionDate:expirationDate:entryDate:exitDate:curatedLabel:
CStrings:
+ "T@\"NSUUID\",R,N,V_visitIdentifier"
+ "T@\"RTMapItem\",R,N,V_originalLabel"
+ "_originalLabel"
+ "_visitIdentifier"
+ "getEarliestDate:"
+ "identifier, %@, submissionDate, %@, expirationDate, %@, visit entry date, %@, visit exit date, %@, visit identifier, %@, original label, %@, curated label, %@"
+ "initWithIdentifier:submissionDate:expirationDate:entryDate:exitDate:visitIdentifier:originalLabel:curatedLabel:"
+ "originalLabel"
+ "visitIdentifier"
- "identifier, %@, submissionDate, %@, expirationDate, %@, entry time, %@, exit time, %@, curated label, %@"

```
