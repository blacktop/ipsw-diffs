## Diagnostic-8340

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8340.appex/Diagnostic-8340`

```diff

 625.2.2.0.0
-  __TEXT.__text: 0x31e0
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_stubs: 0x580
+  __TEXT.__text: 0xb3a8
+  __TEXT.__auth_stubs: 0x870
+  __TEXT.__objc_stubs: 0x820
   __TEXT.__objc_methlist: 0x1c4
-  __TEXT.__const: 0x30
-  __TEXT.__cstring: 0x41c
-  __TEXT.__oslogstring: 0x4d9
+  __TEXT.__const: 0xd0
+  __TEXT.__cstring: 0x1824
+  __TEXT.__oslogstring: 0xaa4
   __TEXT.__objc_classname: 0x52
-  __TEXT.__objc_methname: 0x89d
+  __TEXT.__objc_methname: 0x9ca
   __TEXT.__objc_methtype: 0x147
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x1b0
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x3a0
+  __TEXT.__gcc_except_tab: 0x2b4
+  __TEXT.__unwind_info: 0x178
+  __DATA_CONST.__auth_got: 0x448
+  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0x178
+  __DATA_CONST.__cfstring: 0xf60
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__objc_intobj: 0x198
   __DATA.__objc_const: 0x7a0
-  __DATA.__objc_selrefs: 0x220
+  __DATA.__objc_selrefs: 0x280
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0xc0
-  __DATA.__common: 0x10
-  __DATA.__bss: 0x10
+  __DATA.__data: 0x180
+  __DATA.__common: 0x28
+  __DATA.__bss: 0x38
+  - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
-  Functions: 57
-  Symbols:   90
-  CStrings:  250
+  Functions: 140
+  Symbols:   197
+  CStrings:  519
 
Symbols:
+ _objc_retainBlock
+ _CFDataGetLength
+ _CFHTTPMessageSetHeaderFieldValue
+ _CFNumberCreate
+ _CFStringCreateMutable
+ _HSCSecurePairPearlWithProxy
+ _CFDataGetBytePtr
+ __Unwind_Resume
+ _memcpy
+ __logHandler
+ _objc_release_x26
+ __Block_object_dispose
+ _malloc_type_calloc
+ _CFDictionaryContainsKey
+ _CFStringCompare
+ __NSConcreteStackBlock
+ _HSCGetPearlNonce
+ _IOConnectCallMethod
+ _IORegistryEntryFromPath
+ _CFDictionaryGetValue
+ _CFUUIDCreate
+ _OBJC_CLASS_$_NSNumber
+ _ccder_blob_decode_range
+ _ccder_blob_decode_len
+ _ccsha384_di
+ _CFPropertyListCreateWithData
+ _SavageUpdaterExecCommand
+ _CFHTTPMessageSetBody
+ _ccder_blob_encode_tl
+ _ccder_blob_decode_sequence_tl
+ _CFDictionaryCreateCopy
+ _CFRetain
+ _CFDictionaryGetTypeID
+ _CFHTTPMessageCreateRequest
+ _CFRelease
+ _CFDictionaryAddValue
+ _CFURLCreateWithString
+ _IORegistryEntryCreateCFProperty
+ _CFUUIDCreateString
+ _HSCSecurePairPearl
+ _AMSupportCopyHexStringFromData
+ _AMSupportHttpCopyProxySettings
+ _kAMSupportHttpOptionMaxAttempts
+ _objc_release_x10
+ _qsort
+ _CFDataCreateCopy
+ _CFDataGetTypeID
+ _kCFBooleanTrue
+ ___objc_personality_v0
+ _kAMSupportHttpOptionDisableSSLValidation
+ _AMFDRSealingMapGetFDRDataVersionForDevice
+ _AMSupportLogSetHandler
+ _CFStringGetTypeID
+ _OBJC_CLASS_$_CRPreflightController
+ _ccder_blob_encode_body
+ _kCFBooleanFalse
+ _kAMSupportHttpOptionSocksProxySettings
+ _kAMSupportHttpOptionValidResponses
+ _objc_release_x9
+ _CFDataCreate
+ _CFDataGetBytes
+ _kAMSupportHttpOptionTimeout
+ _syslog
+ _kCFErrorLocalizedDescriptionKey
+ _kCFHTTPVersion1_1
+ _objc_retain
+ _CFErrorCreate
+ _CFStringCreateWithFormat
+ _MGCopyAnswer
+ _AMSupportLogInternal
+ _SavageUpdaterCreate
+ _ccder_sizeof
+ _kCFAllocatorMalloc
+ _malloc
+ _objc_autoreleasePoolPush
+ _CFDataCreateWithBytesNoCopy
+ _CFHTTPMessageCopyAllHeaderFields
+ ___chkstk_darwin
+ _ccder_blob_decode_tag
+ _pearlSeaCookieHandleMessage
+ _SavageUpdaterIsDone
+ ___stdoutp
+ _malloc_type_malloc
+ _kCFTypeDictionaryValueCallBacks
+ _CFStringGetCStringPtr
+ _dispatch_sync
+ _ccdigest
+ _dispatch_queue_create
+ _AMSupportHttpSendSync
+ _CFPropertyListCreateData
+ _CFStringAppend
+ _ccder_blob_decode_tl
+ _objc_autoreleasePoolPop
+ _CFDictionarySetValue
+ _CFGetTypeID
+ _bzero
+ _AMAuthInstallApImg4SetSepNonce
+ _AMAuthInstallSetSigningServerURL
+ _CFDictionaryCreateMutable
+ _kCFNull
+ _kCFTypeDictionaryKeyCallBacks
+ _memcmp
+ _memset_s
+ _AMSupportLogDumpMemory
+ _OBJC_CLASS_$_CRPersonalizationManager
+ _AMSupportCreateSetFromCFIndexArray
+ _CFStringCreateMutableCopy
CStrings:
+ "POST"
+ "^{__CFString=}24@?0r*8Q16"
+ "aksStatus is %!d(MISSING)"
+ "------- SERVER RESPONSE -------\n"
+ "Create xmlData failed, error: %!@(MISSING)"
+ "Failed to request FDR permission"
+ "_HSCHandleMessage"
+ "seaCookieHandleMessage %!d(MISSING) %!p(MISSING) %!z(MISSING)u %!p(MISSING) %!p(MISSING)\n"
+ "createError"
+ "Failed to load savage patch. Error: %!@(MISSING)"
+ "SensorType"
+ "SensorUID: %!@(MISSING)"
+ "ApChipID: %!@(MISSING)"
+ "Failed to exec Savage Updater command: %!@(MISSING)"
+ "SepNonce"
+ "UUID"
+ "Update savage firmware successfully"
+ "SERVER RESPONSE is NULL\n"
+ "ErrorMessage"
+ "(type == kPearlFactorySeaCookieValidateTatsuTicket) || replySize"
+ "Options"
+ "xmlData : %!@(MISSING)"
+ "ApChipID"
+ "Create xmlData failed."
+ "HSCGetPearlNonce"
+ "SensorType : %!@(MISSING)"
+ "Unable to relay response to SEP and obtain information \n"
+ "1.2"
+ "CFPropertyListCreateData failed\n"
+ "Device info dict is %!@(MISSING)"
+ "Failed to pair pearl: %!i(MISSING), error: %!@(MISSING)"
+ "base64EncodedStringWithOptions:"
+ "SIK : %!@(MISSING)"
+ "_HSCHandleMesaMessage"
+ "0x"
+ "HSCSecurePairPearlWithProxy"
+ "SIK"
+ "_HSCHandleMessage Failed"
+ "Failed to create connection options dictionary.\n"
+ "Input argument req_dict is empty or NULL\n"
+ "*replySize >= outData->dataSize"
+ "Creating savage updater ..."
+ "result = %!d(MISSING)\n"
+ "Content-Type"
+ "Failed to get manifest ticket"
+ "Response Dictionary : %!@(MISSING)\n"
+ "getClientAuth"
+ "--------------------------------------------------------------\n"
+ "Setting custom TATSU server URL: %!@(MISSING)"
+ "appropriate command is not present"
+ "enableSSO:"
+ "mesaStatus: %!d(MISSING) Size: %!d(MISSING)"
+ "CameraH10 devices not supported"
+ "Command = %!@(MISSING)\n"
+ "Could not create proxy settings, system default proxy will be used."
+ "Request"
+ "_HSCGetPearlInfo"
+ "%!s(MISSING): %!s(MISSING)"
+ "ReprovisionSensor"
+ "inData"
+ "\terrorString: "
+ "(type == kPearlFactorySeaCookieValidateTatsuTicket) || reply"
+ "Couldn't create OS Log for 'com.apple.BiometricKit.Library-MesaFactory'!\n"
+ "getDefaultAMAuthInstallRef"
+ "Command"
+ "Failed to get pearl nonce with error %!@(MISSING)"
+ "aks"
+ "C7"
+ "Failed to get default AMAuthInstallRef"
+ "ErrorMessage - %!@(MISSING)"
+ "Resetting session\n"
+ "seaCookieHandleMessage, type=%!d(MISSING) -> 0x%!x(MISSING)\n"
+ "FirmwareData"
+ "shouldPersonalizeWithSSOByDefault"
+ "_HSCPairProxy"
+ "%!(BADPREC)%!s(MISSING)"
+ "Content-Length"
+ "Error is empty"
+ "Failed to encode RIK keyBlob to base64 data"
+ "PairProjector"
+ "Content Length Empty"
+ "\terrorCode: "
+ "ApECID"
+ "Pearl Nonce Size: %!d(MISSING)"
+ "RePairingSessionKeyExchange"
+ "Disabling SSL validation"
+ "IOService:/IOResources/AppleKeyStore"
+ "%!X(MISSING)"
+ "seaCookieHandleMessage, type=%!d(MISSING) reply[%!z(MISSING)u] %!(BADPREC)%!P(MISSING)\n"
+ "(type == kMesaFactorySeaCookieMessageS0) || (type == kMesaFactorySeaCookieGenerateNonce) || messageLength"
+ "Empty deviceInfoDict"
+ "Validate tatsu ticket succeeded."
+ "Digest"
+ "signature"
+ "/Library/Caches/com.apple.xbs/Sources/Mesa/AppleBiometricServices/MesaFactoryC/MesaFactoryC.c"
+ "Request data is : %!@(MISSING)\n"
+ "Version"
+ "Savage,Ticket"
+ "pearlSeaCookieHandleMessage, type=%!d(MISSING) -> 0x%!x(MISSING)\n"
+ "%!@(MISSING)\n"
+ "AppleBiometricServices"
+ "Failed to allocate UpdaterOptions."
+ "dataWithBytes:length:"
+ "performNextStage"
+ "/tmp/%!@(MISSING)-from-server"
+ "Unable to get pearl nonce"
+ "DataRef or responseDict is NULL."
+ "i28@?0i8r*12Q20"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) bad 2%!s(MISSING)\n"
+ "isSSR"
+ "pearlSeaCookieHandleMessage %!d(MISSING) %!p(MISSING) %!z(MISSING)u %!p(MISSING) %!p(MISSING)\n"
+ "sik_pub_key is NULL"
+ "HorizonSeaCookieErrorDomain"
+ "Seacookie Pairing URL: %!@(MISSING)"
+ "application/xml"
+ "i24@?0r*8Q16"
+ "pearlSeaCookieHandleMessage, type=%!d(MISSING) reply[%!z(MISSING)u] %!(BADPREC)%!P(MISSING)\n"
+ "Content Length -- empty \n"
+ "------- END CLIENT REQUEST -------\n"
+ "Unknown camera type"
+ "aks-client-queue"
+ "sik_digest is NULL"
+ "AppleKeyStore"
+ "S6"
+ "Savage UID: %!@(MISSING)"
+ "initWithAuthInstallObj:"
+ "SensorUID"
+ "Server returned an "
+ "inputData"
+ "result : %!d(MISSING)"
+ "(type == kPearlFactorySeaCookieMessageS0) || (type == kPearlFactorySeaCookieGenerateNonce) || message"
+ "Protocol Version : %!@(MISSING)"
+ "Failed to sign payload data"
+ "Not supported."
+ "Send request status: %!d(MISSING) http status: %!l(MISSING)d error: %!@(MISSING)\n"
+ "RestoreInternal"
+ "SeaCookiePairingOption"
+ "(type == kMesaFactorySeaCookieMessageS0) || (type == kMesaFactorySeaCookieGenerateNonce) || message"
+ "ErrorCode is String Type"
+ "SensorSN"
+ "SeaCookie server returned HTTP status: %!l(MISSING)d\n"
+ "SensorNonce : %!@(MISSING)"
+ "useProdMasterKey"
+ "Unknown callback type."
+ "mesaInfo"
+ "C5"
+ "Failed to power cycle sensor: %!@(MISSING)"
+ "SensorChipID: %!@(MISSING)"
+ "Signature = %!@(MISSING)\n"
+ "createRequestData"
+ "inputData --> %!@(MISSING) inputSize --> %!l(MISSING)u"
+ "------- END SERVER RESPONSE -------\n"
+ "/tmp/%!@(MISSING)"
+ "Unprovisioned sensor"
+ "Calling pearl patch loading."
+ "Response"
+ "_HSCHandlePearlMessage"
+ "xmlData is not CFDictionary type."
+ "C4"
+ "Failed to enable single sign on"
+ "Failed to get Savage UID"
+ "development-cert"
+ "requestData : %!@(MISSING) responseData : %!@(MISSING)"
+ "HTTP Status == 200. OK\n"
+ "sendRequestSync"
+ "SensorSNUM: %!@(MISSING)"
+ "der_key_validate"
+ "S5"
+ "Unable to get Mesa Information"
+ "(type == kPearlFactorySeaCookieMessageS0) || (type == kPearlFactorySeaCookieGenerateNonce) || messageSize"
+ "PairProjectorFinal"
+ "Request Dictionary Creation failed\n"
+ "seaCookieHandleMessage message[%!z(MISSING)u] %!(BADPREC)%!P(MISSING)\n"
+ "Pearl Nonce: %!@(MISSING)"
+ "Unable to get Pearl Information"
+ "chipID: %!u(MISSING) Size: %!l(MISSING)lu"
+ "getApTicketForSeaCookiePairingWithOptions:pairingTicket:error:"
+ "%!d(MISSING)"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) aks connection failed%!s(MISSING)\n"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) fail%!s(MISSING)\n"
+ "SensorNonce"
+ "SensorSN: %!@(MISSING)"
+ "Failed to create FDR permission string"
+ "X-Apple-SeaCookie-IP"
+ "ErrorString : %!@(MISSING)\n"
+ "Server did not return session cookie"
+ "MesaFactoryC seacookie message handling."
+ "C6"
+ "Failed to initialize personalization manager with error %!@(MISSING)"
+ "Unknown SeaCookie type"
+ "_HSCHandlePearlMessage_block_invoke"
+ "could not create contentLengthStr\n"
+ "LE2kQ7U1iM32AmlhYvlagg"
+ "Failed to create %!s(MISSING) obj::error: %!@(MISSING)"
+ "%!l(MISSING)u"
+ "Payload = %!@(MISSING)\n"
+ "startPairing"
+ "Unable to receive Module Information\n"
+ "Output - Module Function = %!@(MISSING)\n"
+ "SensorSNUM"
+ "SpecVersion"
+ "moduleStatus = %!d(MISSING) reply[%!l(MISSING)u] \n"
+ "size == sizeof(state)"
+ "Invalid Arguments"
+ "SensorChipID"
+ "parseResponse"
+ "sik_pub_key_len is 0"
+ ":"
+ "Unable to parse response data from SeaCookie server\n"
+ "_HSCGetModuleInfo"
+ "HTTP send error: %!d(MISSING)\n"
+ "PearlFactoryLib seacookie message handling."
+ "pearlInfo"
+ "Failed to set TATSU server URL with error %!d(MISSING)"
+ "_HSCSeaCookieHandler"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) bad 1%!s(MISSING)\n"
+ "ApECID: %!@(MISSING)"
+ "Library-MesaFactory"
+ "could not create httpRequest\n"
+ "Failed to create max attempts\n"
+ "S4"
+ "TrustedAccessoryFactory seacookie message handling."
+ "SensorChipID : %!@(MISSING)"
+ "Unable to create Error object\n"
+ "_HSCHandleMessage returned : %!d(MISSING)"
+ "ErrorCode"
+ "pearlStatus: %!d(MISSING) Size: %!d(MISSING)"
+ "XML datalen: %!l(MISSING)u data is : %!@(MISSING)\n"
+ "Failed to create timeout\n"
+ "sign:keyBlob:"
+ "Savage Serial Number: %!@(MISSING)"
+ "Session"
+ "powerCycleSensor:"
+ "(type == kMesaFactorySeaCookieValidateTatsuTicket) || reply"
+ "Failed to set SEP nonce with error %!d(MISSING)"
+ "CFPropertyListCreateData failed : %!@(MISSING)\n"
+ "Failed to exec SavageUpdater Command: %!@(MISSING):%!@(MISSING)"
+ "Failed to find patch files"
+ "------- CLIENT REQUEST -------\n"
+ "SepNonce : %!@(MISSING)"
+ "failed to open connection to %!s(MISSING)\n"
+ "initWithBase64EncodedString:options:"
+ "Unable to send/receive data with SeaCookie server\n"
+ "getSIKString"
+ "unable to create a request \n"
+ "Extracted patch digest: %!@(MISSING)"
+ "PersonalizedFirmwareRootPath"
+ "Savage"
+ "_aks_operation"
+ "Failed to get Savage Serial Number"
+ "Unable to validate tatsu ticket"
+ "_merge_dict_cb"
+ "/private/var/tmp/usr/standalone/firmware/Savage/"
+ "Exiting parse_response : %!d(MISSING)"
+ "FNvQ6lBvJIUcYBzQ8ggOUQ"
+ "Processing Message  %!@(MISSING) --> %!@(MISSING)"
+ "(type == kMesaFactorySeaCookieValidateTatsuTicket) || replySize"
+ "CFDataCreate sik_digest failed"
+ "IODeviceTree:/chosen"
+ "Invalid Argument"
+ "_HSCGetMesaInfo"
+ "callback"
+ "responseDict : %!@(MISSING)"
+ "responseDict NULL. Unable to parse Response\n"
+ "00"
+ "Found patch files successfully"
+ "Create UpdaterOptions successfully, value of ticket is: %!@(MISSING)"
+ "numberWithInteger:"
+ "queryInfo"

```
