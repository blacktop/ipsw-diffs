## iapd

> `/System/Library/PrivateFrameworks/IAP.framework/Support/iapd`

```diff

-  __TEXT.__text: 0xd9b4c
-  __TEXT.__auth_stubs: 0x1d30
+  __TEXT.__text: 0xed658
+  __TEXT.__auth_stubs: 0x2190
   __TEXT.__objc_stubs: 0x4b80
-  __TEXT.__init_offsets: 0x1c
-  __TEXT.__objc_methlist: 0x1964
-  __TEXT.__gcc_except_tab: 0x7b04
-  __TEXT.__const: 0x5e90
-  __TEXT.__cstring: 0x13eeb
+  __TEXT.__init_offsets: 0x20
+  __TEXT.__objc_methlist: 0x1974
+  __TEXT.__gcc_except_tab: 0x7d7c
+  __TEXT.__const: 0x74f0
+  __TEXT.__cstring: 0x14ca4
   __TEXT.__objc_methname: 0x5306
   __TEXT.__objc_classname: 0x268
-  __TEXT.__objc_methtype: 0xea1
-  __TEXT.__unwind_info: 0x4628
-  __DATA_CONST.__const: 0x7808
-  __DATA_CONST.__cfstring: 0x73a0
+  __TEXT.__objc_methtype: 0xede
+  __TEXT.__unwind_info: 0x4d68
+  __DATA_CONST.__const: 0x8930
+  __DATA_CONST.__cfstring: 0x7460
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA_CONST.__auth_got: 0xeb0
-  __DATA_CONST.__got: 0x9b8
+  __DATA_CONST.__auth_got: 0x10e0
+  __DATA_CONST.__got: 0x9f0
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x2e18
   __DATA.__objc_selrefs: 0x1568
   __DATA.__objc_ivar: 0x2d4
   __DATA.__objc_data: 0x8c0
-  __DATA.__data: 0x2428
-  __DATA.__bss: 0x7b8
-  __DATA.__common: 0x788
+  __DATA.__data: 0x2468
+  __DATA.__bss: 0x910
+  __DATA.__common: 0x7a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 3812
-  Symbols:   797
-  CStrings:  4009
+  Functions: 4274
+  Symbols:   869
+  CStrings:  4090
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_ivar : content changed
~ __DATA.__objc_data : content changed
Symbols:
+ _BTSessionDetachWithQueue
+ _CC_SHA1_Final
+ _CC_SHA1_Init
+ _CC_SHA1_Update
+ _EraseSigningContext
+ _FinalizeSigningContext
+ _IapAuthGetAppCert
+ _InitSigningContext
+ _UpdateSigningContext
+ __ZNKSt3__119__shared_weak_count13__get_deleterERKSt9type_info
+ __ZNSt3__119__shared_weak_count14__release_weakEv
+ __ZNSt3__119__shared_weak_count4lockEv
+ __ZNSt3__119__shared_weak_countD2Ev
+ __ZNSt3__122__libcpp_verbose_abortEPKcz
+ __ZNSt3__1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
+ __ZTINSt3__119__shared_weak_countE
+ _dirname
+ _feof
+ _fflush
+ _fgetc
+ _fileno
+ _fread
+ _fseek
+ _ftruncate
+ _rename
+ _stat
+ _statfs
+ _strdup
+ _strerror
+ _xmlAddChild
+ _xmlBufferContent
+ _xmlBufferCreate
+ _xmlBufferFree
+ _xmlBufferLength
+ _xmlC14NDocDumpMemory
+ _xmlCleanupParser
+ _xmlCopyNode
+ _xmlCopyNodeList
+ _xmlDocGetRootElement
+ _xmlDocSetRootElement
+ _xmlFreeDoc
+ _xmlFreeNode
+ _xmlFreeTextReader
+ _xmlFreeTextWriter
+ _xmlInitParser
+ _xmlNewDoc
+ _xmlNewNode
+ _xmlNewTextWriterMemory
+ _xmlNewTextWriterTree
+ _xmlNodeAddContent
+ _xmlNodeDumpOutput
+ _xmlOutputBufferClose
+ _xmlOutputBufferCreateIO
+ _xmlParseFile
+ _xmlReaderForIO
+ _xmlSetProp
+ _xmlStrcmp
+ _xmlTextReaderConstName
+ _xmlTextReaderConstValue
+ _xmlTextReaderHasAttributes
+ _xmlTextReaderIsEmptyElement
+ _xmlTextReaderMoveToNextAttribute
+ _xmlTextReaderNodeType
+ _xmlTextReaderRead
+ _xmlTextWriterEndDocument
+ _xmlTextWriterEndElement
+ _xmlTextWriterFlush
+ _xmlTextWriterStartElement
+ _xmlTextWriterWriteAttribute
+ _xmlTextWriterWriteBase64
+ _xmlTextWriterWriteElement
+ _xmlTextWriterWriteFormatElement
CStrings:
+ "                lingo 0x%x (%p): eventMask=0x%x persist=0x%x"
+ "%.2f"
+ "%04d-%02d-%02d %02d;%02d;%02d.xml"
+ "%lu.p7"
+ "%lu.plist"
+ "%s:%d !secStatus\n"
+ "%s:%d 0 != xmlStatus\n"
+ "%s:%d 1 != bytesRead\n"
+ "%s:%d CIapLingoStorage::OpeniPodFeatureFile invalid feature type: %d !"
+ "%s:%d IPodFileError_NoError != status\n"
+ "%s:%d LingoMicrophone:DeviceHandle devValid=%d handle=%hhx pMicLingo=%p\n"
+ "%s:%d NULL == pOpenFile->fData\n"
+ "%s:%d NULL == pOpenFile->pXmlSig\n"
+ "%s:%d NotifyEvent: handle: %03d, pCurFile: %hhx\n"
+ "%s:%d RemoteUI Object does not match, cannot handle EnterRemoteUIMode! %p != %p\n"
+ "%s:%d StorageLingo object(%hhx) or handle(%hhx) is NULL! Cannot TransmitPacketDelaySleep\n"
+ "%s:%d Update: %d %hhx %d\n"
+ "%s:%d WriteiPodFileData XmlSig.Update: status: 0x%08X, size: 0x%08X\n"
+ "%s:%d dataLen != writeLen\n"
+ "%s:%d dataLen == 0\n"
+ "%s:%d devPort(%hhx) != m_perPortInfo(%hhx)\n"
+ "%s:%d writeLen != xmlBuffLen\n"
+ "%s:%d: XmlSigData::CompleteSignedFile WriteSignature() failed or root tag not ready for signature"
+ "%s:%d: XmlSigData::WriteSignature File verification failed skipping signature"
+ "%s:%d: workoutDataXMLGenericTagParseCntx::SendDataToConsumers SigData->GetOutStreamCntlr() failed"
+ "%s:%d: workoutDataXMLrootTagParseCntx::CompleteParseProc currElem->GetCompleteTagString() failed"
+ "%s:%d: workoutDataXMLrootTagParseCntx::CompleteParseProc sigData->AccumulateC14N() failed"
+ "&amp;"
+ "&gt;"
+ "&lt;"
+ ".."
+ ".tmp"
+ "/"
+ "/Accessories"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/iapd/iapd/IAP/Source/IapLingoStorage.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/iapd/iapd/iSL/Source/XMLParse/iMAXMLFileSrcStream.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/iapd/iapd/iSL/Source/XMLSignature/workoutDataXMLGenericTagParseCntx.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/iapd/iapd/iSL/Source/XMLSignature/xmlSigData.cpp"
+ "/Tags"
+ "/Trainer/Workouts/Empeds"
+ "1.0"
+ "</"
+ "<ipodInfo><openTime>%04d-%02d-%02dT%02d:%02d:%02d%c%02d:%02d</openTime><closeTime>%04d-%02d-%02dT%02d:%02d:%02d%c%02d:%02d</closeTime>"
+ "<model>%s</model><softwareVersion>%d.%d.%d</softwareVersion><serialNumber>%s</serialNumber></ipodInfo>"
+ "CloseiPodFeatureFile(handle = %u)\n"
+ "Deleting zero-length feature file %s\n"
+ "ERROR - %s:%s - couldn't find accessory details for connectionID=0x%x"
+ "ERROR - %s:%s - couldn't find transport for connectionID=0x%x"
+ "ERROR: %s:%d Invalid certificate delimiter fields\n"
+ "GYM_WORKOUT_COMPLETED_MSG"
+ "GYM_WORKOUT_COMPLETED_TITLE"
+ "Nuking %s\n"
+ "OpeniPodFeatureFile(feature = %d, options = 0x%x, handle = %u) == %d\n"
+ "Renaming %s to %s failed: %s\n"
+ "SETTINGS_STRING"
+ "TGym::DeserializeCurrentGymUserInformation userID invalid\n"
+ "TGym::DeserializeGymInformation failed to read userCount\n"
+ "TGym::DeserializeGymInformation failed to read userIndex\n"
+ "TGym::DeserializeGymInformation userName invalid\n"
+ "Unlinking %s failed: %s\n"
+ "bad_weak_ptr was thrown in -fno-exceptions mode"
+ "data->CompleteSignedFile() failed\n"
+ "http://www.w3.org/2000/09/xmldsig#"
+ "http://www.w3.org/2000/09/xmldsig#enveloped-signature"
+ "http://www.w3.org/2000/09/xmldsig#rsa-sha1"
+ "http://www.w3.org/2000/09/xmldsig#sha1"
+ "http://www.w3.org/2001/10/xml-exc-c14n#"
+ "iMAXMLOutStreamCntlr::BeginInnermostElemSerializer null mInnermostElem"
+ "iMAXMLParseCntxLookup::CheckSetTableLength: null table ptr!"
+ "iMAXMLParseCntxLookup::Init failed to create parse context"
+ "iMAXMLParseContext::CreateTagOutputSerializer iMAXMLOutStreamCntlr->CreateElementSerializer failed"
+ "iMAXMLParseContextManager::AddContext nil Context param"
+ "iMAXMLParseCtlr::ParseLoopEx: Failed to create xmltextreader object\n"
+ "inStream->InitStream failed\n"
+ "parser->DoParse() failed\n"
+ "prefs:root=victoria"
+ "r"
+ "w+"
+ "{map<unsigned int, NSNumber *, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, NSNumber *>>>=\"__tree_\"{__tree<std::__value_type<unsigned int, NSNumber *>, std::__map_value_compare<unsigned int, std::pair<const unsigned int, NSNumber *>, std::less<unsigned int>>, std::allocator<std::pair<const unsigned int, NSNumber *>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{map<unsigned short, IAPSession *, std::less<unsigned short>, std::allocator<std::pair<const unsigned short, IAPSession *>>>=\"__tree_\"{__tree<std::__value_type<unsigned short, IAPSession *>, std::__map_value_compare<unsigned short, std::pair<const unsigned short, IAPSession *>, std::less<unsigned short>>, std::allocator<std::pair<const unsigned short, IAPSession *>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{shared_ptr<ISL::IPodEventSender>=\"__ptr_\"^{IPodEventSender}\"__cntrl_\"^{__shared_weak_count}}"
+ "\xf0%"
- "                lingo 0x%x (%hhx): eventMask=0x%x persist=0x%x"
- "%s:%d LingoMicrophone:DeviceHandle devValid=%d handle=%hhx pMicLingo=%hhx\n"
- "%s:%d RemoteUI Object does not match, cannot handle EnterRemoteUIMode! %hhx != %hhx\n"
- "^{IPodEventSender=^^?}"
- "{map<unsigned int, NSNumber *, std::less<unsigned int>, std::allocator<std::pair<const unsigned int, NSNumber *> > >=\"__tree_\"{__tree<std::__value_type<unsigned int, NSNumber *>, std::__map_value_compare<unsigned int, std::pair<const unsigned int, NSNumber *>, std::less<unsigned int> >, std::allocator<std::pair<const unsigned int, NSNumber *> > >=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
- "{map<unsigned short, IAPSession *, std::less<unsigned short>, std::allocator<std::pair<const unsigned short, IAPSession *> > >=\"__tree_\"{__tree<std::__value_type<unsigned short, IAPSession *>, std::__map_value_compare<unsigned short, std::pair<const unsigned short, IAPSession *>, std::less<unsigned short> >, std::allocator<std::pair<const unsigned short, IAPSession *> > >=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
- "\xe5"

```
