## Diagnostic-8268

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8268.appex/Diagnostic-8268`

```diff

 397.140.7.0.0
-  __TEXT.__text: 0xaa8
-  __TEXT.__auth_stubs: 0x170
-  __TEXT.__objc_stubs: 0x200
+  __TEXT.__text: 0x8934
+  __TEXT.__auth_stubs: 0x6a0
+  __TEXT.__objc_stubs: 0x400
   __TEXT.__objc_methlist: 0xac
-  __TEXT.__cstring: 0x168
-  __TEXT.__oslogstring: 0xa8
+  __TEXT.__cstring: 0x1483
+  __TEXT.__oslogstring: 0x5ab
   __TEXT.__objc_classname: 0x3c
-  __TEXT.__objc_methname: 0x3da
+  __TEXT.__objc_methname: 0x4e4
   __TEXT.__objc_methtype: 0x111
-  __TEXT.__unwind_info: 0x7c
-  __DATA_CONST.__auth_got: 0xc0
-  __DATA_CONST.__got: 0x8
-  __DATA_CONST.__cfstring: 0x1a0
+  __TEXT.__const: 0x50
+  __TEXT.__unwind_info: 0x114
+  __DATA_CONST.__auth_got: 0x358
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0x128
+  __DATA_CONST.__cfstring: 0xb60
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x20
-  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__objc_classrefs: 0x50
+  __DATA_CONST.__objc_intobj: 0x108
   __DATA.__objc_const: 0x5b0
-  __DATA.__objc_selrefs: 0xc8
+  __DATA.__objc_selrefs: 0x130
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0xc0
+  __DATA.__data: 0x184
+  __DATA.__bss: 0x30
+  __DATA.__common: 0x28
+  - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /usr/lib/libFDR.dylib

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 15
-  Symbols:   42
-  CStrings:  113
+  Functions: 85
+  Symbols:   161
+  CStrings:  359
 
Symbols:
+ _AMAuthInstallApImg4SetSepNonce
+ _AMAuthInstallSetSigningServerURL
+ _AMAuthInstallSsoEnable
+ _AMAuthInstallSsoInitialize
+ _AMFDRSealingMapGetFDRDataVersionForDevice
+ _AMSupportCopyHexStringFromData
+ _AMSupportCreateSetFromCFIndexArray
+ _AMSupportHttpCopyProxySettings
+ _AMSupportHttpSendSync
+ _AMSupportLogDumpMemory
+ _AMSupportLogInternal
+ _AMSupportLogSetHandler
+ _CFDataCreate
+ _CFDataCreateCopy
+ _CFDataCreateWithBytesNoCopy
+ _CFDataGetBytePtr
+ _CFDataGetBytes
+ _CFDataGetLength
+ _CFDataGetTypeID
+ _CFDictionaryAddValue
+ _CFDictionaryContainsKey
+ _CFDictionaryCreateCopy
+ _CFDictionaryCreateMutable
+ _CFDictionaryGetTypeID
+ _CFDictionaryGetValue
+ _CFDictionarySetValue
+ _CFErrorCreate
+ _CFGetTypeID
+ _CFHTTPMessageCreateRequest
+ _CFHTTPMessageSetBody
+ _CFHTTPMessageSetHeaderFieldValue
+ _CFNumberCreate
+ _CFPropertyListCreateData
+ _CFPropertyListCreateWithData
+ _CFRelease
+ _CFStringAppend
+ _CFStringCreateMutable
+ _CFStringCreateMutableCopy
+ _CFStringCreateWithFormat
+ _CFStringGetTypeID
+ _CFUUIDCreate
+ _CFUUIDCreateString
+ _HSCGetMesaNonce
+ _HSCSecureProvisionMesaWithUID
+ _HSCSecureProvisionMesaWithUIDProxy
+ _IOConnectCallMethod
+ _IOConnectCallStructMethod
+ _IOObjectRelease
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryFromPath
+ _IOServiceClose
+ _IOServiceGetMatchingService
+ _IOServiceMatching
+ _IOServiceOpen
+ _OBJC_CLASS_$_CRPersonalizationManager
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSString
+ __NSConcreteGlobalBlock
+ __NSConcreteStackBlock
+ ___chkstk_darwin
+ ___osLogPearlLib
+ ___osLogPearlLibTrace
+ ___stderrp
+ ___stdoutp
+ __logHandler
+ __os_log_default
+ _bzero
+ _calloc
+ _ccder_blob_decode_len
+ _ccder_blob_decode_range
+ _ccder_blob_decode_sequence_tl
+ _ccder_blob_decode_tag
+ _ccder_blob_decode_tl
+ _ccder_blob_encode_body
+ _ccder_blob_encode_tl
+ _ccder_sizeof
+ _ccdigest
+ _ccsha384_di
+ _dispatch_once
+ _dispatch_queue_create
+ _dispatch_sync
+ _fprintf
+ _free
+ _kAMSupportHttpOptionDisableSSLValidation
+ _kAMSupportHttpOptionMaxAttempts
+ _kAMSupportHttpOptionSocksProxySettings
+ _kAMSupportHttpOptionTimeout
+ _kAMSupportHttpOptionValidResponses
+ _kCFAllocatorDefault
+ _kCFAllocatorMalloc
+ _kCFBooleanFalse
+ _kCFBooleanTrue
+ _kCFErrorLocalizedDescriptionKey
+ _kCFHTTPVersion1_1
+ _kCFNull
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _kIOMainPortDefault
+ _kIOMasterPortDefault
+ _mach_task_self_
+ _malloc
+ _malloc_type_calloc
+ _malloc_type_malloc
+ _memcmp
+ _memcpy
+ _memmove
+ _memset_s
+ _objc_alloc
+ _objc_release
+ _objc_release_x25
+ _objc_release_x27
+ _objc_release_x28
+ _os_log_create
+ _pearlSeaCookieHandleMessage
+ _qsort
+ _syslog
CStrings:
+ "\terrorCode: "
+ "\terrorString: "
+ "%!X(MISSING)"
+ "%!l(MISSING)u"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) bad 1%!s(MISSING)\n"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) bad 2%!s(MISSING)\n"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) fail%!s(MISSING)\n"
+ "(type == kMesaFactorySeaCookieMessageS0) || (type == kMesaFactorySeaCookieGenerateNonce) || message"
+ "(type == kMesaFactorySeaCookieMessageS0) || (type == kMesaFactorySeaCookieGenerateNonce) || messageLength"
+ "(type == kMesaFactorySeaCookieValidateTatsuTicket) || reply"
+ "(type == kMesaFactorySeaCookieValidateTatsuTicket) || replySize"
+ "(type == kPearlFactorySeaCookieMessageS0) || message"
+ "(type == kPearlFactorySeaCookieMessageS0) || messageSize"
+ "*bufferSize"
+ "*replySize >= outData->dataSize"
+ "------- SERVER RESPONSE -------\n%!(BADPREC)%!s(MISSING)------- END SERVER RESPONSE -------\n"
+ "------------------------------ \nRequest Content: \n%!@(MISSING)\n ------------------------------ \n"
+ "--------------------------------------------------------------\n"
+ "-[MesaPairer start]"
+ "/Library/Caches/com.apple.xbs/Sources/Mesa/AppleBiometricServices/MesaFactoryC/MesaFactoryC.c"
+ "/Library/Caches/com.apple.xbs/Sources/Pearl_Kernel/PearlFactoryLib/PearlFactoryLib.m"
+ "/tmp/%!@(MISSING)"
+ "/tmp/%!@(MISSING)-from-server"
+ "0x"
+ "1.2"
+ ":"
+ "ApChipID"
+ "ApChipID: %!@(MISSING)"
+ "ApECID"
+ "ApECID: %!@(MISSING)"
+ "AppleBiometricServices"
+ "AppleKeyStore"
+ "ApplePearlSEPDriver"
+ "AssertMacros: %!s(MISSING) (value = 0x%!l(MISSING)x), %!s(MISSING) file: %!s(MISSING), line: %!d(MISSING)\n\n"
+ "AssertMacros: %!s(MISSING) (value = 0x%!l(MISSING)x), %!s(MISSING) file: %!s(MISSING), line: %!d(MISSING)\n\n"
+ "C5"
+ "C6"
+ "C7"
+ "CFDataCreate sik_digest failed"
+ "CFPropertyListCreateData failed\n"
+ "CFPropertyListCreateData failed : %!@(MISSING)\n"
+ "Calling pearl patch loading."
+ "Command"
+ "Command = %!@(MISSING)\n"
+ "Content Length -- empty \n"
+ "Content Length Empty"
+ "Content-Length"
+ "Content-Type"
+ "Could not create proxy settings, system default proxy will be used."
+ "Couldn't create OS Log for 'com.apple.BiometricKit.Library-MesaFactory'!\n"
+ "Couldn't create OS Log for 'com.apple.BiometricKit.Library-PearlFactory'!\n"
+ "Create xmlData failed, error: %!@(MISSING)"
+ "Create xmlData failed."
+ "DataRef or responseDict is NULL."
+ "Disabling SSL validation"
+ "Error is empty"
+ "ErrorCode"
+ "ErrorCode is String Type"
+ "ErrorMessage"
+ "ErrorMessage - %!@(MISSING)"
+ "ErrorString : %!@(MISSING)\n"
+ "Exiting parse_response : %!d(MISSING)"
+ "Fail to provision mesa: %!i(MISSING) error: %!@(MISSING)"
+ "Failed load SSOClient.framework"
+ "Failed load SSOClient.framework"
+ "Failed to create connection options dictionary.\n"
+ "Failed to create max attempts\n"
+ "Failed to create timeout\n"
+ "Failed to enable single sign on"
+ "Failed to enable single sign on"
+ "Failed to get default AMAuthInstallRef"
+ "Failed to get default AMAuthInstallRef"
+ "Failed to get mesa nonce with error %!@(MISSING)"
+ "Failed to initialize personalization manager with error %!@(MISSING)"
+ "Failed to set SEP nonce with error %!d(MISSING)"
+ "Failed to set SEP nonce with error %!d(MISSING)"
+ "Failed to set TATSU server URL with error %!d(MISSING)"
+ "Failed to set TATSU server URL with error %!d(MISSING)"
+ "HSCGetMesaNonce"
+ "HSCSecureProvisionMesaWithUIDProxy"
+ "HTTP Status == 200. OK\n"
+ "HTTP send error: %!d(MISSING)\n"
+ "HorizonSeaCookieErrorDomain"
+ "IODeviceTree:/chosen"
+ "IOService:/IOResources/AppleKeyStore"
+ "Input argument req_dict is empty or NULL\n"
+ "Invalid Argument"
+ "Invalid Arguments"
+ "Library-MesaFactory"
+ "Library-PearlFactory"
+ "Mesa Module serial number: %!@(MISSING)"
+ "Mesa Nonce Size: %!d(MISSING)"
+ "Mesa Nonce: %!@(MISSING)"
+ "Mesa sensor serial number: %!@(MISSING)"
+ "MesaFactoryC seacookie message handling."
+ "No Error"
+ "Not supported."
+ "Output - Module Function = %!@(MISSING)\n"
+ "POST"
+ "PairSensor"
+ "Payload = %!@(MISSING)\n"
+ "PearlFactoryLib seacookie message handling."
+ "Processing Message  %!@(MISSING) --> %!@(MISSING)"
+ "Request"
+ "Request Dictionary Creation failed\n"
+ "Request data is : %!@(MISSING)\n"
+ "Resetting session\n"
+ "Response"
+ "Response Dictionary : %!@(MISSING)\n"
+ "S5"
+ "S6"
+ "S7"
+ "SERVER RESPONSE is NULL\n"
+ "SIK"
+ "SIK : %!@(MISSING)"
+ "SeaCookie server returned HTTP status: %!l(MISSING)d\n"
+ "Send request status: %!d(MISSING) http status: %!l(MISSING)d error: %!@(MISSING)\n"
+ "SensorChipID"
+ "SensorChipID: %!@(MISSING)"
+ "SensorSN"
+ "SensorSN: %!@(MISSING)"
+ "SensorSNUM"
+ "SensorSNUM: %!@(MISSING)"
+ "SensorType"
+ "SensorType : %!@(MISSING)"
+ "SensorUID"
+ "SensorUID: %!@(MISSING)"
+ "SepNonce"
+ "SepNonce : %!@(MISSING)"
+ "Server did not return session cookie"
+ "Server returned an "
+ "Session"
+ "SessionKeyExch"
+ "Setting custom tatsu server URL: %!@(MISSING)"
+ "SpecVersion"
+ "TrustedAccessoryFactory seacookie message handling."
+ "UUID"
+ "Unable to create Error object\n"
+ "Unable to get Mesa Information"
+ "Unable to get Pearl Information"
+ "Unable to get current mesa provisioning state"
+ "Unable to get mesa nonce"
+ "Unable to get mesa provisioning state"
+ "Unable to get mesa serial number"
+ "Unable to parse response data from SeaCookie server\n"
+ "Unable to receive Module Information\n"
+ "Unable to relay response to Mesa and obtain information \n"
+ "Unable to send/receive data with SeaCookie server\n"
+ "Unable to validate tatsu ticket"
+ "Unknown SeaCookie type"
+ "Unknown callback type."
+ "Using Apple Connect"
+ "Validate tatsu ticket succeeded."
+ "XML datalen: %!l(MISSING)u data is : %!@(MISSING)\n"
+ "_HSCGetMesaInfo"
+ "_HSCGetModuleInfo"
+ "_HSCGetPearlInfo"
+ "_HSCHandleMesaMessage"
+ "_HSCHandleMessage"
+ "_HSCHandleMessage Failed"
+ "_HSCHandleMessage returned : %!d(MISSING)"
+ "_HSCHandlePearlMessage"
+ "_HSCHandlePearlMessage_block_invoke"
+ "_HSCPairProxy"
+ "_HSCSeaCookieHandler"
+ "_merge_dict_cb"
+ "absoluteString"
+ "aks"
+ "aks-client-queue"
+ "aksStatus is %!d(MISSING)"
+ "application/xml"
+ "appropriate command is not present"
+ "buffer"
+ "bufferSize"
+ "callback"
+ "chipID: %!u(MISSING) Size: %!l(MISSING)lu"
+ "cmd"
+ "code"
+ "com.apple.BiometricKit"
+ "could not create contentLengthStr\n"
+ "could not create httpRequest\n"
+ "createError"
+ "createRequestData"
+ "dataWithBytes:length:"
+ "der_key_validate"
+ "development-cert"
+ "err == 0 "
+ "failed to open connection to %!s(MISSING)\n"
+ "getApTicketForMesaPairing:error:"
+ "getClientAuth"
+ "getDefaultAMAuthInstallRef"
+ "getInnermostNSError:"
+ "getModuleSerialNumber %!p(MISSING) %!p(MISSING)\n"
+ "getModuleSerialNumber -> %!{(MISSING)errno}d\n"
+ "getSIKString"
+ "getSensorProvisioningState %!p(MISSING)\n"
+ "getSensorProvisioningState -> %!{(MISSING)errno}d %!d(MISSING)\n"
+ "getSensorSerialNumber %!p(MISSING) %!p(MISSING)\n"
+ "getSensorSerialNumber -> %!{(MISSING)errno}d\n"
+ "i"
+ "i28@?0i8r*12Q20"
+ "inData"
+ "initWithAuthInstallObj:"
+ "initWithBytes:length:encoding:"
+ "inputData"
+ "inputData --> %!@(MISSING) inputSize --> %!l(MISSING)u"
+ "localizedDescription"
+ "mesaInfo"
+ "mesaModuleSerialNumber"
+ "mesaSensorPreviousState"
+ "mesaSensorProvisioningState"
+ "mesaSensorSerialNumber"
+ "mesaStatus: %!d(MISSING) Size: %!d(MISSING)"
+ "moduleStatus = %!d(MISSING) reply[%!l(MISSING)u] \n"
+ "numberWithInteger:"
+ "numberWithUnsignedInt:"
+ "parseResponse"
+ "pearlInfo"
+ "pearlSeaCookieHandleMessage %!d(MISSING) %!p(MISSING) %!z(MISSING)u %!p(MISSING) %!p(MISSING)\n"
+ "pearlSeaCookieHandleMessage, type=%!d(MISSING) -> 0x%!x(MISSING)\n"
+ "pearlSeaCookieHandleMessage, type=%!d(MISSING) reply[%!z(MISSING)u] %!(BADPREC)%!P(MISSING)\n"
+ "pearlStatus: %!d(MISSING) Size: %!d(MISSING)"
+ "reply"
+ "replySize"
+ "requestData : %!@(MISSING) responseData : %!@(MISSING)"
+ "responseDict : %!@(MISSING)"
+ "responseDict NULL. Unable to parse Response\n"
+ "result : %!d(MISSING)"
+ "result = %!d(MISSING)\n"
+ "seaCookieHandleMessage %!d(MISSING) %!p(MISSING) %!z(MISSING)u %!p(MISSING) %!p(MISSING)\n"
+ "seaCookieHandleMessage message[%!z(MISSING)u] %!(BADPREC)%!P(MISSING)\n"
+ "seaCookieHandleMessage, type=%!d(MISSING) -> 0x%!x(MISSING)\n"
+ "seaCookieHandleMessage, type=%!d(MISSING) reply[%!z(MISSING)u] %!(BADPREC)%!P(MISSING)\n"
+ "sendRequestSync"
+ "service"
+ "sik_digest is NULL"
+ "sik_pub_key is NULL"
+ "sik_pub_key_len is 0"
+ "size == sizeof(state)"
+ "startPairing"
+ "stringWithFormat:"
+ "unable to create a request \n"
+ "useProdMasterKey"
+ "v8@?0"
+ "xmlData : %!@(MISSING)"
+ "xmlData is not CFDictionary type."

```
