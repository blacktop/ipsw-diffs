## iWorkFileFormat

> `/System/Library/PrivateFrameworks/iWorkXPC.framework/XPCServices/iWorkFileFormat.xpc/iWorkFileFormat`

```diff

-20.0.0.0.0
-  __TEXT.__text: 0x1637f4
+22.1.0.0.0
+  __TEXT.__text: 0x16778c
   __TEXT.__auth_stubs: 0x1740
-  __TEXT.__objc_stubs: 0x8cc0
+  __TEXT.__objc_stubs: 0x8de0
   __TEXT.__init_offsets: 0x40
-  __TEXT.__objc_methlist: 0x5988
-  __TEXT.__const: 0xa4c8
+  __TEXT.__objc_methlist: 0x59e0
+  __TEXT.__const: 0xa5d0
   __TEXT.__objc_classname: 0x10e0
-  __TEXT.__objc_methname: 0xe01e
-  __TEXT.__objc_methtype: 0x27e8
-  __TEXT.__gcc_except_tab: 0xc514
-  __TEXT.__cstring: 0x1125d
-  __TEXT.__oslogstring: 0x6406
+  __TEXT.__objc_methname: 0xe1f0
+  __TEXT.__objc_methtype: 0x2800
+  __TEXT.__gcc_except_tab: 0xc608
+  __TEXT.__cstring: 0x10ddd
+  __TEXT.__oslogstring: 0x6521
   __TEXT.__ustring: 0x76
-  __TEXT.__unwind_info: 0x8714
+  __TEXT.__unwind_info: 0x8798
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0xbb8
-  __DATA_CONST.__got: 0x358
+  __DATA_CONST.__got: 0x360
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xe488
+  __DATA_CONST.__const: 0xe6c0
   __DATA_CONST.__cfstring: 0x2f00
   __DATA_CONST.__objc_classlist: 0x380
   __DATA_CONST.__objc_catlist: 0x118
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x4a0
+  __DATA_CONST.__objc_superrefs: 0x300
   __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0xb278
-  __DATA.__objc_selrefs: 0x3360
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x498
-  __DATA.__objc_superrefs: 0x300
+  __DATA.__objc_const: 0xb2a8
+  __DATA.__objc_selrefs: 0x33b8
   __DATA.__objc_ivar: 0x624
   __DATA.__objc_data: 0x2300
-  __DATA.__data: 0x2308
-  __DATA.__bss: 0xc70
-  __DATA.__common: 0x21b0
+  __DATA.__data: 0x2350
+  __DATA.__bss: 0xc98
+  __DATA.__common: 0x2218
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 8153
-  Symbols:   4278
-  CStrings:  4808
+  Functions: 8249
+  Symbols:   4317
+  CStrings:  4826
 
Symbols:
+ _CGImageSourceCreateWithURL
+ _UTTagClassFilenameExtension
+ _UTTagClassMIMEType
+ _UTTypeData
+ _UTTypeDirectory
+ __ZN3TSP23_Rect_default_instance_E
+ __ZN3TSP25_Pose3D_default_instance_E
+ __ZN3TSP4Rect14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE
+ __ZN3TSP4Rect5ClearEv
+ __ZN3TSP4Rect8CopyFromERKN6google8protobuf7MessageE
+ __ZN3TSP4Rect9MergeFromERKN6google8protobuf7MessageE
+ __ZN3TSP4Rect9MergeFromERKS0_
+ __ZN3TSP4RectD0Ev
+ __ZN3TSP4RectD1Ev
+ __ZN3TSP4RectD2Ev
+ __ZN3TSP6Pose3D14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE
+ __ZN3TSP6Pose3D5ClearEv
+ __ZN3TSP6Pose3D8CopyFromERKN6google8protobuf7MessageE
+ __ZN3TSP6Pose3D9MergeFromERKN6google8protobuf7MessageE
+ __ZN3TSP6Pose3D9MergeFromERKS0_
+ __ZN3TSP6Pose3DD0Ev
+ __ZN3TSP6Pose3DD1Ev
+ __ZN6google8protobuf5Arena18CreateMaybeMessageIN3TSP4RectEJEEEPT_PS1_DpOT0_
+ __ZN6google8protobuf5Arena18CreateMaybeMessageIN3TSP6Pose3DEJEEEPT_PS1_DpOT0_
+ __ZNK3TSP4Rect11GetMetadataEv
+ __ZNK3TSP4Rect12ByteSizeLongEv
+ __ZNK3TSP4Rect13IsInitializedEv
+ __ZNK3TSP4Rect13SetCachedSizeEi
+ __ZNK3TSP4Rect18_InternalSerializeEPhPN6google8protobuf2io19EpsCopyOutputStreamE
+ __ZNK3TSP4Rect30RequiredFieldsByteSizeFallbackEv
+ __ZNK3TSP6Pose3D11GetMetadataEv
+ __ZNK3TSP6Pose3D12ByteSizeLongEv
+ __ZNK3TSP6Pose3D13IsInitializedEv
+ __ZNK3TSP6Pose3D13SetCachedSizeEi
+ __ZNK3TSP6Pose3D18_InternalSerializeEPhPN6google8protobuf2io19EpsCopyOutputStreamE
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_
+ __ZTIN3TSP4RectE
+ __ZTIN3TSP6Pose3DE
+ __ZTSN3TSP4RectE
+ __ZTSN3TSP6Pose3DE
+ __ZTVN3TSP4RectE
+ __ZTVN3TSP6Pose3DE
+ _scc_info_Pose3D_TSPMessages_2eproto
+ _scc_info_Rect_TSPMessages_2eproto
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_mmRKS4_
- _kUTTagClassFilenameExtension
- _kUTTypeData
- _kUTTypeDirectory
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/messages/src/TSPDatabaseMessages.pb.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/messages/src/TSPMessages.pb.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/any.pb.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/api.pb.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/arena.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/descriptor.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/descriptor.pb.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/descriptor_database.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/duration.pb.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/dynamic_message.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/empty.pb.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/extension_set.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/extension_set_heavy.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/field_mask.pb.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/generated_message_reflection.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/generated_message_util.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/io/coded_stream.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/io/tokenizer.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/io/zero_copy_stream.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/io/zero_copy_stream_impl_lite.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/map_field.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/message.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/message_lite.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/reflection_ops.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/source_context.pb.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/struct.pb.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/stubs/common.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/stubs/stringpiece.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/stubs/strutil.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/stubs/substitute.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/text_format.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/timestamp.pb.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/type.pb.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/wire_format.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/wire_format_lite.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/google/protobuf/wrappers.pb.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/NSData_TSPersistence.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/NSURL_TSPersistence.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPAVAssetResourceLoaderDelegate.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPArchiveMessages.pb.cc"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPCGDataConsumer.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPCompressionComponentWriteChannel.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPCryptoComponentWriteChannel.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPCryptoInfo.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPCryptoReadChannel.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPCryptoTranscodeReadChannel.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPDataCopyProvider.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPDataStorageWriteResult.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPDatabase.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPDatabaseObject.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPDirectoryPackage.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPDirectoryPackageDataWriter.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPDirectoryPackageWriter.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPDocumentProperties.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPDocumentRevision.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPFilePackage.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPFilePackageWriter.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPMemoryReadChannel.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPObjectStateIdentifier.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPPackage.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPPackageConverter.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPPackageWriter.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPPackageWriterComponentWriteChannel.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPSnappyComponentWriteChannel.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPSnappyReadChannel.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPSnappySource.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPTemporaryObjectContextDelegate.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPVersion.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/persistence/src/TSPZipFileWriteChannel.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/NSArrayAdditions.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/NSDictionaryAdditions.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/NSError_TSUAdditions.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/NSException_TSUAdditions.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/NSFileManager_TSUAdditions.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/NSIndexSet_TSUAdditions.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/NSKeyedArchiver_TSUAdditions.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/NSObject_TSUAdditions.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/NSProgress_TSUAdditions.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/NSPropertyListSerialization_TSUtility.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/NSSetAdditions.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/NSString_TSUAdditions.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/NSURL_TSUAdditions.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/NSUUID_TSUAdditions.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/TSUBufferedReadChannel.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/TSUCast.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/TSUCompressionReadChannel.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/TSUDatabase.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/TSUExtendedAttribute.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/TSUFileIOChannel.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/TSUIOUtils.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/TSUNoCopyDictionary.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/TSUReadChannelInputStreamAdapter.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/TSUSafeSaveAssistant.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/TSUTemporaryDirectory.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/TSUUUIDPath.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/TSUZipArchive.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/TSUZipFileArchive.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/TSUZipFileWriter.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/TSUZipInflateReadChannel.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/TSUZipReadChannel.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/TSUZipWriter.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/sf/SFUBufferedInputStream.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/sf/SFUCryptoInputStream.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/sf/SFUCryptoOutputStream.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/sf/SFUCryptoUtils.mm"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/sf/SFUCryptor.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/sf/SFUDataRepresentation.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/sf/SFUFileDataRepresentation.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/sf/SFUFileInputStream.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/sf/SFUFileOutputStream.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/sf/SFUHash.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/sf/SFUMemoryOutputStream.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/sf/SFUOffsetInputStream.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/sf/SFUZipArchive.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/sf/SFUZipArchiveFileDataRepresentation.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/sf/SFUZipEntry.m"
+ "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/shared/utility/sf/SFUZipInflateInputStream.m"
+ "About to perform file coordination to create image source from %@:"
+ "Could not set modificationDate. success=%d targetURL=%@ errorClass=%{public}@, domain=%{public}@, code=%zd (%@) "
+ "Failed to coordinate access to URL: %@ error: errorClass=%{public}@, domain=%{public}@, code=%zd (%@) "
+ "T@\"<NSFilePresenter>\",?,R,N"
+ "T@\"NSDictionary\",?,R,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSUUID\",?,R,N"
+ "T@\"SFUCryptoKey\",?,R"
+ "T@\"TSPDocumentLoadValidationPolicy\",?,R,N"
+ "T@\"TSPDocumentSaveValidationPolicy\",?,R,N"
+ "TB,?,R,N"
+ "Wrong data size (%zu) for TSUZipEndOfCentralDirectoryRecord (size: %zu)"
+ "^{CGImageSource=}16@0:8"
+ "coordinateReadingItemAtURL:options:error:byAccessor:"
+ "failToSaveIfUpdateDataModificationDateFails"
+ "shouldLogAssertionBacktrace"
+ "tsu_UTIMimeType"
+ "tsu_UTTypeCopyPreferredTagWithClass:"
+ "tsu_allFilenameExtensionIdentifiersForTag"
+ "tsu_createImageSourceFromURLAfterForcingFileCoordination"
+ "tsu_isDynamic"
+ "tsu_preferredIdentifierForTagClass:conformingToUTI:"
+ "tsu_stringWithNormalizedSpaces"
+ "updateDataModificationDate"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/messages/src/TSPDatabaseMessages.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/messages/src/TSPMessages.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/any.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/api.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/arena.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/descriptor.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/descriptor.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/descriptor_database.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/duration.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/dynamic_message.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/empty.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/extension_set.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/extension_set_heavy.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/field_mask.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/generated_message_reflection.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/generated_message_util.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/io/coded_stream.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/io/tokenizer.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/io/zero_copy_stream.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/io/zero_copy_stream_impl_lite.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/map_field.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/message.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/message_lite.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/reflection_ops.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/source_context.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/struct.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/stubs/common.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/stubs/stringpiece.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/stubs/strutil.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/stubs/substitute.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/text_format.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/timestamp.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/type.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/wire_format.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/wire_format_lite.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/google/protobuf/wrappers.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/NSData_TSPersistence.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/NSURL_TSPersistence.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPAVAssetResourceLoaderDelegate.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPArchiveMessages.pb.cc"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPCGDataConsumer.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPCompressionComponentWriteChannel.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPCryptoComponentWriteChannel.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPCryptoInfo.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPCryptoReadChannel.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPCryptoTranscodeReadChannel.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPDataCopyProvider.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPDataStorageWriteResult.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPDatabase.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPDatabaseObject.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPDirectoryPackage.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPDirectoryPackageDataWriter.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPDirectoryPackageWriter.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPDocumentProperties.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPDocumentRevision.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPFilePackage.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPFilePackageWriter.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPMemoryReadChannel.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPObjectStateIdentifier.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPPackage.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPPackageConverter.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPPackageWriter.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPPackageWriterComponentWriteChannel.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPSnappyComponentWriteChannel.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPSnappyReadChannel.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPSnappySource.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPTemporaryObjectContextDelegate.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPVersion.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/persistence/src/TSPZipFileWriteChannel.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/NSArrayAdditions.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/NSDictionaryAdditions.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/NSError_TSUAdditions.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/NSException_TSUAdditions.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/NSFileManager_TSUAdditions.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/NSIndexSet_TSUAdditions.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/NSKeyedArchiver_TSUAdditions.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/NSObject_TSUAdditions.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/NSProgress_TSUAdditions.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/NSPropertyListSerialization_TSUtility.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/NSSetAdditions.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/NSString_TSUAdditions.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/NSURL_TSUAdditions.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/NSUUID_TSUAdditions.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/TSUBufferedReadChannel.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/TSUCast.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/TSUCompressionReadChannel.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/TSUDatabase.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/TSUExtendedAttribute.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/TSUFileIOChannel.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/TSUIOUtils.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/TSUNoCopyDictionary.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/TSUReadChannelInputStreamAdapter.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/TSUSafeSaveAssistant.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/TSUTemporaryDirectory.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/TSUUUIDPath.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/TSUZipArchive.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/TSUZipFileArchive.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/TSUZipFileWriter.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/TSUZipInflateReadChannel.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/TSUZipReadChannel.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/TSUZipWriter.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/sf/SFUBufferedInputStream.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/sf/SFUCryptoInputStream.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/sf/SFUCryptoOutputStream.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/sf/SFUCryptoUtils.mm"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/sf/SFUCryptor.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/sf/SFUDataRepresentation.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/sf/SFUFileDataRepresentation.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/sf/SFUFileInputStream.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/sf/SFUFileOutputStream.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/sf/SFUHash.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/sf/SFUMemoryOutputStream.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/sf/SFUOffsetInputStream.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/sf/SFUZipArchive.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/sf/SFUZipArchiveFileDataRepresentation.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/sf/SFUZipEntry.m"
- "/Library/Caches/com.apple.xbs/Sources/iWorkXPC/iwork/src/shared/utility/sf/SFUZipInflateInputStream.m"
- "T@\"<NSFilePresenter>\",R,N"
- "T@\"NSDictionary\",R,N"
- "T@\"SFUCryptoKey\",R"
- "T@\"TSPDocumentLoadValidationPolicy\",R,N"
- "T@\"TSPDocumentSaveValidationPolicy\",R,N"
- "Wrong data size for TSUZipEndOfCentralDirectoryRecord"

```
