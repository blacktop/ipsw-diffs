## hangreporter

> `/usr/libexec/hangreporter`

```diff

-281.2.0.0.0
-  __TEXT.__text: 0x3377c
-  __TEXT.__auth_stubs: 0xe60
-  __TEXT.__objc_stubs: 0x2860
+288.0.0.0.0
+  __TEXT.__text: 0x34248
+  __TEXT.__auth_stubs: 0xe70
+  __TEXT.__objc_stubs: 0x28e0
   __TEXT.__objc_methlist: 0xc54
   __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x2912c
-  __TEXT.__oslogstring: 0x3c0c
+  __TEXT.__cstring: 0x2978e
+  __TEXT.__oslogstring: 0x3ebe
   __TEXT.__gcc_except_tab: 0x3ec
-  __TEXT.__objc_methname: 0x4737
+  __TEXT.__objc_methname: 0x4777
   __TEXT.__objc_classname: 0xdf
   __TEXT.__objc_methtype: 0x74b
   __TEXT.__unwind_info: 0x40c
-  __DATA_CONST.__auth_got: 0x740
-  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__auth_got: 0x748
+  __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x1168
-  __DATA_CONST.__cfstring: 0x3f20
+  __DATA_CONST.__cfstring: 0x3f40
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x180
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x2098
-  __DATA.__objc_selrefs: 0xde8
-  __DATA.__objc_classrefs: 0x178
-  __DATA.__objc_superrefs: 0x50
+  __DATA.__objc_selrefs: 0xe08
   __DATA.__objc_ivar: 0x220
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x4a8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 3A03BB6C-3F05-3CE3-9478-BFF69D75A397
-  Functions: 524
-  Symbols:   320
-  CStrings:  4782
+  UUID: 0BA9A546-DC7C-3F06-823F-E15F617BB21A
+  Functions: 525
+  Symbols:   319
+  CStrings:  4826
 
Symbols:
+ _CFBundleCopyBundleURL
+ _OBJC_CLASS_$_LSApplicationExtensionRecord
+ _OBJC_CLASS_$_LSApplicationRecord
- _LSInternalApplicationType
- _LSSystemApplicationType
- _OBJC_CLASS_$_LSApplicationProxy
- _OBJC_CLASS_$_LSPlugInKitProxy
CStrings:
+ "ASPFTLParseBufferToCxt: GCReadSequential(1106): (#14) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: GCReadSequential(1106): Cannot add 14 elements to context"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsReadSectors(1042): (#15) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsReadSectors(1042): Cannot add 15 elements to context"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsSnapshot(1041): (#31) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsSnapshot(1041): Cannot add 31 elements to context"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsV2(1040): (#31) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsV2(1040): Cannot add 31 elements to context"
+ "ASPFTLParseBufferToCxt: cbdrAborts(696) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: cbdrFullyDone(699) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: cbdrResumeSent(689) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: cbdrSkippedBlocks(758) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: gcPDusterDestinations(721) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: gcPDusterWrites(722) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: gcwamp(1116): (#32) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: gcwamp(1116): Cannot add 32 elements to context"
+ "ASPFTLParseBufferToCxt: hostReadSequential(1105): (#14) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: hostReadSequential(1105): Cannot add 14 elements to context"
+ "Adding hang [%d] %llu-%llu (%llums) to removal list in favor of overlapping [%d] %llu-%llu (%llums) (1p prefer fence if other is <1s longer)"
+ "Adding hang [%d] %llu-%llu (%llums) to removal list in favor of overlapping [%d] %llu-%llu (%llums) (3p prefer fence)"
+ "Adding hang [%d] %llu-%llu (%llums) to removal list in favor of overlapping [%d] %llu-%llu (%llums) (prefer longer hangs)"
+ "Could not rename %{public}@ to %{public}@ due to error %@. Attempting to remove the file"
+ "Could not rename %{public}@ to %{public}@ due to error %@. Attempting to remove the file."
+ "GCReadSequential"
+ "GCReadSequential_"
+ "No extension record for %@: %@"
+ "No parent record for %@"
+ "No parent url for %@"
+ "Process:%{public}@ hang duration %0.0fms is greater than %llums, fetching IOReg GPU AGX SchedulerState info"
+ "Removing %lu hangs in favor of overlapping [%d] %llu-%llu (%llums)"
+ "Removing hang [%d] %llu-%llu (%llums) in favor of overlapping [%d] %llu-%llu (%llums) (1p prefer fence if other is <1s longer)"
+ "Removing hang [%d] %llu-%llu (%llums) in favor of overlapping [%d] %llu-%llu (%llums) (1p prefer fence if other is <1s longer) (not removing %lu on removal list)"
+ "Removing hang [%d] %llu-%llu (%llums) in favor of overlapping [%d] %llu-%llu (%llums) (3p prefer fence)"
+ "Removing hang [%d] %llu-%llu (%llums) in favor of overlapping [%d] %llu-%llu (%llums) (3p prefer fence) (not removing %lu on removal list)"
+ "Removing hang [%d] %llu-%llu (%llums) in favor of overlapping [%d] %llu-%llu (%llums) (prefer longer hangs)"
+ "Removing hang [%d] %llu-%llu (%llums) in favor of overlapping [%d] %llu-%llu (%llums) (prefer longer hangs) (not removing %lu on removal list)"
+ "Skipping non-tailspin file: %{public}@"
+ "Successfully created directory at path %@"
+ "URL"
+ "[%d] %llu-%llu (%llums) does not overlap any other hangs"
+ "appex"
+ "bandsAgeBinsReadSectors"
+ "bandsAgeBinsReadSectors_"
+ "bandsAgeBinsSnapshot"
+ "bandsAgeBinsSnapshot_"
+ "bandsAgeBinsV2"
+ "bandsAgeBinsV2_"
+ "cbdrAborts"
+ "cbdrFullyDone"
+ "cbdrResumeSent"
+ "cbdrSkippedBlocks"
+ "containingBundleRecord"
+ "developerType"
+ "distributorID"
+ "distributorInfo"
+ "distributor_id"
+ "gcPDusterDestinations"
+ "gcPDusterWrites"
+ "gcwamp"
+ "gcwamp_"
+ "hostReadSequential"
+ "hostReadSequential_"
+ "iTunesMetadata"
+ "initWithURL:allowPlaceholder:error:"
+ "initWithURL:error:"
+ "objectForKey:ofClass:"
+ "storeCohortWithError:"
+ "storeItemIdentifier"
- "ASPFTLParseBufferToCxt: fwaHistogram(913): (#10) cfg elements != (%d) buffer elements"
- "ASPFTLParseBufferToCxt: fwaHistogram(913): Cannot add 10 elements to context"
- "Adding hang [%d] %llu-%llu to removal list in favor of overlapping [%d] %llu-%llu (prefer fence)"
- "Adding hang [%d] %llu-%llu to removal list in favor of overlapping [%d] %llu-%llu (prefer longer hangs)"
- "Could not rename %@ to %@ due to error %@. Attempting to remove the file"
- "Could not rename %@ to %@ due to error %@. Attempting to remove the file."
- "Hidden"
- "Process:%@ hang duration %0.0fms is greater than %llums, fetching IOReg GPU AGX SchedulerState info"
- "Removing %lu hangs in favor of overlapping [%d] %llu-%llu"
- "Removing hang [%d] %llu-%llu in favor of overlapping [%d] %llu-%llu (prefer fence)"
- "Removing hang [%d] %llu-%llu in favor of overlapping [%d] %llu-%llu (prefer fence) (not removing %lu on removal list)"
- "Removing hang [%d] %llu-%llu in favor of overlapping [%d] %llu-%llu (prefer longer hangs)"
- "Removing hang [%d] %llu-%llu in favor of overlapping [%d] %llu-%llu (prefer longer hangs) (not removing %lu on removal list)"
- "Skipping non-tailspin file: %@"
- "Sucessfully created directory at path %@"
- "[%d] %llu-%llu does not overlap any other hangs"
- "applicationProxyForIdentifier:"
- "applicationType"
- "containingBundle"
- "foundBackingBundle"
- "fwaHistogram"
- "fwaHistogram_"
- "itemID"
- "pluginKitProxyForIdentifier:"
- "storeCohortMetadata"

```
