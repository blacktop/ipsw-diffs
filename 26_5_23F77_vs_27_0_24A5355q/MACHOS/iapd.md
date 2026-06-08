## iapd

> `/System/Library/PrivateFrameworks/IAP.framework/Support/iapd`

```diff

-2176.100.2.0.0
-  __TEXT.__text: 0xde0c8
-  __TEXT.__auth_stubs: 0x2140
-  __TEXT.__objc_stubs: 0x4ea0
+2181.0.3.0.0
+  __TEXT.__text: 0xd9b80
+  __TEXT.__auth_stubs: 0x1d30
+  __TEXT.__objc_stubs: 0x4b80
   __TEXT.__init_offsets: 0x1c
-  __TEXT.__objc_methlist: 0x1a4c
-  __TEXT.__const: 0x6c60
-  __TEXT.__gcc_except_tab: 0x1610
-  __TEXT.__cstring: 0x1521a
-  __TEXT.__objc_methname: 0x572f
-  __TEXT.__objc_classname: 0x2c8
-  __TEXT.__objc_methtype: 0xee4
-  __TEXT.__unwind_info: 0x19f8
-  __DATA_CONST.__auth_got: 0x10b8
-  __DATA_CONST.__got: 0x9e0
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x8278
-  __DATA_CONST.__cfstring: 0x7680
-  __DATA_CONST.__objc_classlist: 0xf8
+  __TEXT.__objc_methlist: 0x1964
+  __TEXT.__gcc_except_tab: 0x7b04
+  __TEXT.__const: 0x5e90
+  __TEXT.__cstring: 0x13eeb
+  __TEXT.__objc_methname: 0x5306
+  __TEXT.__objc_classname: 0x268
+  __TEXT.__objc_methtype: 0xea1
+  __TEXT.__unwind_info: 0x4628
+  __DATA_CONST.__const: 0x7808
+  __DATA_CONST.__cfstring: 0x73a0
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0xc0
+  __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x3118
-  __DATA.__objc_selrefs: 0x1658
-  __DATA.__objc_ivar: 0x2ec
-  __DATA.__objc_data: 0x9b0
-  __DATA.__data: 0x2490
-  __DATA.__bss: 0xd48
-  __DATA.__common: 0x8e8
+  __DATA_CONST.__auth_got: 0xeb0
+  __DATA_CONST.__got: 0x9b8
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA.__objc_const: 0x2e18
+  __DATA.__objc_selrefs: 0x1568
+  __DATA.__objc_ivar: 0x2d4
+  __DATA.__objc_data: 0x8c0
+  __DATA.__data: 0x2428
+  __DATA.__bss: 0x7b8
+  __DATA.__common: 0x788
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: EED90B72-E285-3EF8-A178-B0A636EB9214
-  Functions: 4132
-  Symbols:   866
-  CStrings:  4193
+  UUID: 309348CC-0001-3022-9928-B4F87BF1E335
+  Functions: 3812
+  Symbols:   797
+  CStrings:  4009
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainBlock
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x27
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x7
+ _objc_retain_x9
- _CC_SHA1_Final
- _CC_SHA1_Init
- _CC_SHA1_Update
- _CFUserNotificationReceiveResponse
- _EraseSigningContext
- _FinalizeSigningContext
- _IapAuthGetAppCert
- _InitSigningContext
- _OBJC_CLASS_$_NSAutoreleasePool
- _OBJC_CLASS_$_NSDistributedNotificationCenter
- _SBUserNotificationDismissOnLock
- _SBUserNotificationDontDismissOnUnlock
- _UpdateSigningContext
- __Block_object_assign
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcm
- __ZNSt3__1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
- _dirname
- _dispatch_retain
- _feof
- _fflush
- _fgetc
- _fileno
- _fmtcheck
- _fread
- _fseek
- _ftruncate
- _kCFUserNotificationIconURLKey
- _mach_error_string
- _objc_autorelease
- _objc_release_x10
- _objc_setProperty_nonatomic
- _rename
- _sprintf
- _stat
- _statfs
- _strdup
- _strerror
- _xmlAddChild
- _xmlBufferContent
- _xmlBufferCreate
- _xmlBufferFree
- _xmlBufferLength
- _xmlC14NDocDumpMemory
- _xmlCleanupParser
- _xmlCopyNode
- _xmlCopyNodeList
- _xmlDocGetRootElement
- _xmlDocSetRootElement
- _xmlFreeDoc
- _xmlFreeNode
- _xmlFreeTextReader
- _xmlFreeTextWriter
- _xmlInitParser
- _xmlNewDoc
- _xmlNewNode
- _xmlNewTextWriterMemory
- _xmlNewTextWriterTree
- _xmlNodeAddContent
- _xmlNodeDumpOutput
- _xmlOutputBufferClose
- _xmlOutputBufferCreateIO
- _xmlParseFile
- _xmlReaderForIO
- _xmlSetProp
- _xmlStrcmp
- _xmlTextReaderConstName
- _xmlTextReaderConstValue
- _xmlTextReaderHasAttributes
- _xmlTextReaderIsEmptyElement
- _xmlTextReaderMoveToNextAttribute
- _xmlTextReaderNodeType
- _xmlTextReaderRead
- _xmlTextWriterEndDocument
- _xmlTextWriterEndElement
- _xmlTextWriterFlush
- _xmlTextWriterStartElement
- _xmlTextWriterWriteAttribute
- _xmlTextWriterWriteBase64
- _xmlTextWriterWriteElement
- _xmlTextWriterWriteFormatElement
- _xpc_release
- _xpc_retain
CStrings:
+ "1"
+ "2"
+ "can't open socket"
+ "\xe5"
- "%.2f"
- "%02X"
- "%04d-%02d-%02d %02d;%02d;%02d.xml"
- "%lu.p7"
- "%lu.plist"
- "%s:%d !secStatus\n"
- "%s:%d 0 != xmlStatus\n"
- "%s:%d 1 != bytesRead\n"
- "%s:%d CIapLingoSports::ProcessCmd packet transID = 0!\n"
- "%s:%d CIapLingoSports::ProcessCmd timeoutStatus != 0!\n"
- "%s:%d CIapLingoStorage::OpeniPodFeatureFile invalid feature type: %d !"
- "%s:%d IAP_EVENT_CLASS_MODE_CHANGE with Event Type:%ld\n"
- "%s:%d IPodFileError_NoError != status\n"
- "%s:%d NULL == pOpenFile->fData\n"
- "%s:%d NULL == pOpenFile->pXmlSig\n"
- "%s:%d NotifyEvent: handle: %03d, pCurFile: %hhx\n"
- "%s:%d StorageLingo object(%hhx) or handle(%hhx) is NULL! Cannot TransmitPacketDelaySleep\n"
- "%s:%d Update: %d %hhx %d\n"
- "%s:%d WriteiPodFileData XmlSig.Update: status: 0x%08X, size: 0x%08X\n"
- "%s:%d dataLen != writeLen\n"
- "%s:%d dataLen == 0\n"
- "%s:%d devPort(%hhx) != m_pDevPortObj(%hhx)\n"
- "%s:%d devPort(%hhx) != m_perPortInfo(%hhx)\n"
- "%s:%d unexpected line in on saved !\n"
- "%s:%d userCount == 0\n"
- "%s:%d writeLen != xmlBuffLen\n"
- "%s:%d: XmlSigData::CompleteSignedFile WriteSignature() failed or root tag not ready for signature"
- "%s:%d: XmlSigData::WriteSignature File verification failed skipping signature"
- "%s:%d: workoutDataXMLGenericTagParseCntx::SendDataToConsumers SigData->GetOutStreamCntlr() failed"
- "%s:%d: workoutDataXMLrootTagParseCntx::CompleteParseProc currElem->GetCompleteTagString() failed"
- "%s:%d: workoutDataXMLrootTagParseCntx::CompleteParseProc sigData->AccumulateC14N() failed"
- "%s:%s-%d found another port %s that supports Display Port on same connector, with acc details %s, %s, %s"
- "&amp;"
- "&gt;"
- "&lt;"
- ".."
- ".tmp"
- "/"
- "/Accessories"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/iapd/iapd/IAP/Source/IapLingoSports.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/iapd/iapd/IAP/Source/IapLingoStorage.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/iapd/iapd/iSL/Source/XMLParse/iMAXMLFileSrcStream.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/iapd/iapd/iSL/Source/XMLSignature/workoutDataXMLGenericTagParseCntx.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/iapd/iapd/iSL/Source/XMLSignature/xmlSigData.cpp"
- "/System/Library/PreferencePanes/Security.prefPane/Contents/Resources/FileVault.icns"
- "/Tags"
- "/Trainer/Workouts/Empeds"
- "1.0"
- "<%@: %p, displayName: %@, certSerialString: %@>"
- "</"
- "<ipodInfo><openTime>%04d-%02d-%02dT%02d:%02d:%02d%c%02d:%02d</openTime><closeTime>%04d-%02d-%02dT%02d:%02d:%02d%c%02d:%02d</closeTime>"
- "<model>%s</model><softwareVersion>%d.%d.%d</softwareVersion><serialNumber>%s</serialNumber></ipodInfo>"
- "@\"NSUserDefaults\""
- "ACCAccessoryAuthorizationEntry"
- "ACCAccessoryAuthorizationStore"
- "ACCAuthorizationManager"
- "ACCKnownAccessoriesDidChangeNotification"
- "ACC_AUTHORIZATION_NOTIFICATION_ALLOW"
- "ACC_AUTHORIZATION_NOTIFICATION_CHARGE_ONLY"
- "ACC_AUTHORIZATION_NOTIFICATION_DONT_ALLOW"
- "ACC_AUTHORIZATION_NOTIFICATION_HEADER"
- "ACC_AUTHORIZATION_NOTIFICATION_HEADER_NO_NAME"
- "ACC_AUTHORIZATION_NOTIFICATION_MESSAGE"
- "ACC_AUTHORIZATION_NOTIFICATION_MESSAGE_NO_NAME"
- "Authorization response time: %dms\n"
- "Authorization status: %d"
- "BypassTrustDialog"
- "Bypassing user authorization..."
- "CIapLingoSports::NotifyEvent: ERROR: Unknown event: %d !\n"
- "CheckForVideoResourceOverride"
- "CloseiPodFeatureFile(handle = %u)\n"
- "Could not configure USB mode: %s\n"
- "Could not disable ACC power: %s\n"
- "Could not enable ACC power: %s\n"
- "Couldn't get cert serial for user authorization!\n"
- "Current USB Connection Active: %d\n"
- "Current USB Connection Type: %d\n"
- "Deleting zero-length feature file %s\n"
- "Done waiting for user authorization!"
- "Drive Kit Plus"
- "EnableTrustDialog"
- "GYM_WORKOUT_COMPLETED_MSG"
- "GYM_WORKOUT_COMPLETED_TITLE"
- "KnownAccessories"
- "Nuking %s\n"
- "OpeniPodFeatureFile(feature = %d, options = 0x%x, handle = %u) == %d\n"
- "Q24@0:8@16"
- "Q36@0:8@16B24@28"
- "Renaming %s to %s failed: %s\n"
- "SETTINGS_STRING"
- "T@\"NSMutableDictionary\",&,N,V_notificationDictMutable"
- "T@\"NSString\",&,N,V_certSerialString"
- "T@\"NSString\",&,N,V_displayName"
- "T@\"NSUserDefaults\",&,N,V_userDefaults"
- "TB,N,V_authorized"
- "TB,N,V_bypassAuthorization"
- "TGym::DeserializeCurrentGymUserInformation userID invalid\n"
- "TGym::DeserializeGymInformation failed to read userCount\n"
- "TGym::DeserializeGymInformation failed to read userIndex\n"
- "TGym::DeserializeGymInformation userName invalid\n"
- "Toggling USB connection for 1250ms...\n"
- "USB mode: %d\n"
- "Unlinking %s failed: %s\n"
- "Waiting for user authorization..."
- "_authorized"
- "_bypassAuthorization"
- "_certSerialString"
- "_displayName"
- "_notificationDictMutable"
- "_userDefaults"
- "authorizationEntryForCertSerial:"
- "authorizationEntryForCertSerial:withAccessoryDict:"
- "authorizationStatus: %lu"
- "authorizationStatusForCertSerial:"
- "authorized"
- "boolForKey:"
- "bypassAuthorization"
- "certSerialString"
- "com.apple.IAP"
- "com.mbrdna.drivestyle"
- "data->CompleteSignedFile() failed\n"
- "dictionaryForKey:"
- "displayName"
- "forceRequestAuthorizationForCertSerial:withName:providesPower:completionHandler:"
- "http://www.w3.org/2000/09/xmldsig#"
- "http://www.w3.org/2000/09/xmldsig#enveloped-signature"
- "http://www.w3.org/2000/09/xmldsig#rsa-sha1"
- "http://www.w3.org/2000/09/xmldsig#sha1"
- "http://www.w3.org/2001/10/xml-exc-c14n#"
- "iMAXMLOutStreamCntlr::BeginInnermostElemSerializer null mInnermostElem"
- "iMAXMLParseCntxLookup::CheckSetTableLength: null table ptr!"
- "iMAXMLParseCntxLookup::Init failed to create parse context"
- "iMAXMLParseContext::CreateTagOutputSerializer iMAXMLOutStreamCntlr->CreateElementSerializer failed"
- "iMAXMLParseContextManager::AddContext nil Context param"
- "iMAXMLParseCtlr::ParseLoopEx: Failed to create xmltextreader object\n"
- "inStream->InitStream failed\n"
- "knownAccessoriesDidChange:"
- "notificationDictMutable"
- "parser->DoParse() failed\n"
- "prefs:root=victoria"
- "promptResponse: %lu"
- "promptUserForAuthorizationOfAccessoryWithName:providesPower:certSerial:"
- "r"
- "removeAccessory:"
- "requestAuthorizationForCertSerial:withName:providesPower:completionHandler:"
- "setAuthorized:"
- "setBypassAuthorization:"
- "setCertSerialString:"
- "setDisplayName:"
- "setNotificationDictMutable:"
- "setUserDefaults:"
- "setWithSet:"
- "sharedStore"
- "standardUserDefaults"
- "storeAccessory:"
- "storedAccessories"
- "storedCertSerialStrings"
- "synchronize"
- "userDefaults"
- "v12@?0B8"
- "v44@0:8@16@24B32@?36"
- "w+"

```
