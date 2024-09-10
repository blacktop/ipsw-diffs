## Diagnostic-8268

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8268.appex/Diagnostic-8268`

```diff

 625.2.2.0.0
-  __TEXT.__text: 0xb5c
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__objc_stubs: 0x220
+  __TEXT.__text: 0x90b8
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_stubs: 0x4c0
   __TEXT.__objc_methlist: 0xbc
-  __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x170
-  __TEXT.__oslogstring: 0xbb
+  __TEXT.__const: 0xb8
+  __TEXT.__cstring: 0x1640
+  __TEXT.__oslogstring: 0x58a
   __TEXT.__objc_classname: 0x3c
-  __TEXT.__objc_methname: 0x437
+  __TEXT.__objc_methname: 0x5b3
   __TEXT.__objc_methtype: 0x11b
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0xd8
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__cfstring: 0x1c0
+  __TEXT.__unwind_info: 0x130
+  __DATA_CONST.__auth_got: 0x368
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0x150
+  __DATA_CONST.__cfstring: 0xca0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__objc_classrefs: 0x10
+  __DATA_CONST.__objc_intobj: 0x108
   __DATA.__objc_const: 0x5e0
-  __DATA.__objc_selrefs: 0xd8
+  __DATA.__objc_selrefs: 0x160
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0xc0
+  __DATA.__data: 0x184
+  __DATA.__common: 0x28
+  __DATA.__bss: 0x38
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
-  Symbols:   46
-  CStrings:  121
+  Functions: 85
+  Symbols:   164
+  CStrings:  389
 
Symbols:
+ _memset_s
+ _pearlSeaCookieHandleMessage
+ _kAMSupportHttpOptionTimeout
+ _AMSupportCopyHexStringFromData
+ _AMSupportCreateSetFromCFIndexArray
+ _CFHTTPMessageCreateRequest
+ ___osLogPearlLibTrace
+ _ccder_blob_decode_len
+ _AMSupportHttpCopyProxySettings
+ _CFDictionaryGetValue
+ _kCFAllocatorMalloc
+ _fprintf
+ _AMSupportLogInternal
+ _CFDictionaryCreateMutable
+ _CFStringAppend
+ _CFStringCreateMutable
+ __os_log_default
+ ___stderrp
+ ___stdoutp
+ _bzero
+ _AMAuthInstallApImg4SetSepNonce
+ _CFHTTPMessageSetBody
+ ___chkstk_darwin
+ _ccder_sizeof
+ _CFDataCreateWithBytesNoCopy
+ _IORegistryEntryCreateCFProperty
+ _kCFNull
+ _ccder_blob_decode_tag
+ _AMAuthInstallSetSigningServerURL
+ _CFStringCompare
+ _CFUUIDCreate
+ _CFUUIDCreateString
+ _ccsha384_di
+ _memcmp
+ _HSCSecureProvisionMesaWithUIDProxy
+ _kIOMasterPortDefault
+ _objc_release
+ _AMSupportLogSetHandler
+ __NSConcreteGlobalBlock
+ _kCFErrorLocalizedDescriptionKey
+ _memmove
+ _CFDictionaryContainsKey
+ _kCFTypeDictionaryValueCallBacks
+ _kIOMainPortDefault
+ _CFPropertyListCreateData
+ _CFPropertyListCreateWithData
+ _CFRetain
+ _ccder_blob_encode_body
+ _CFDictionaryGetTypeID
+ _OBJC_CLASS_$_CRPersonalizationManager
+ _OBJC_CLASS_$_CRPreflightController
+ _kCFBooleanTrue
+ _CFStringCreateMutableCopy
+ _calloc
+ _AMSupportHttpSendSync
+ _CFDataCreateCopy
+ _CFDictionarySetValue
+ _CFGetTypeID
+ _IOServiceGetMatchingService
+ __logHandler
+ _mach_task_self_
+ _CFDataGetLength
+ _CFNumberCreate
+ _malloc_type_calloc
+ _malloc
+ _CFDataGetBytePtr
+ _OBJC_CLASS_$_NSNumber
+ _dispatch_sync
+ _free
+ _memcpy
+ _CFDictionaryAddValue
+ _CFStringCreateWithFormat
+ _OBJC_CLASS_$_NSString
+ _malloc_type_malloc
+ _ccder_blob_decode_tl
+ _kAMSupportHttpOptionMaxAttempts
+ _objc_retainBlock
+ _CFDataGetTypeID
+ _IOConnectCallMethod
+ _IOObjectRelease
+ _IORegistryEntryFromPath
+ __NSConcreteStackBlock
+ _AMSupportLogDumpMemory
+ _IOServiceMatching
+ _ccder_blob_encode_tl
+ _HSCSecureProvisionMesaWithUID
+ _kAMSupportHttpOptionSocksProxySettings
+ _CFDataGetBytes
+ _CFErrorCreate
+ _ccdigest
+ _CFDictionaryCreateCopy
+ _CFHTTPMessageCopyAllHeaderFields
+ _CFHTTPMessageSetHeaderFieldValue
+ _CFStringGetTypeID
+ _ccder_blob_decode_sequence_tl
+ _kAMSupportHttpOptionDisableSSLValidation
+ _dispatch_once
+ _dispatch_queue_create
+ _CFRelease
+ _IOServiceOpen
+ ___osLogPearlLib
+ _ccder_blob_decode_range
+ _AMFDRSealingMapGetFDRDataVersionForDevice
+ _kCFBooleanFalse
+ _syslog
+ _objc_release_x28
+ _qsort
+ _IOServiceClose
+ _kAMSupportHttpOptionValidResponses
+ _kCFAllocatorDefault
+ _kCFHTTPVersion1_1
+ _IOConnectCallStructMethod
+ _OBJC_CLASS_$_NSFileManager
+ _kCFTypeDictionaryKeyCallBacks
+ _os_log_create
+ _HSCGetMesaNonce
+ _OBJC_CLASS_$_NSMutableDictionary
+ _CFDataCreate
CStrings:
+ "HorizonSeaCookieErrorDomain"
+ "IODeviceTree:/chosen"
+ "Unable to get mesa serial number"
+ "_HSCHandlePearlMessage_block_invoke"
+ "(type == kMesaFactorySeaCookieValidateTatsuTicket) || reply"
+ "No Error"
+ "Response"
+ "Unable to validate tatsu ticket"
+ "------- END SERVER RESPONSE -------\n"
+ "localizedDescription"
+ "result : %!d(MISSING)"
+ "sik_pub_key_len is 0"
+ "seaCookieHandleMessage %!d(MISSING) %!p(MISSING) %!z(MISSING)u %!p(MISSING) %!p(MISSING)\n"
+ "sign:keyBlob:"
+ "ApECID: %!@(MISSING)"
+ "Unable to receive Module Information\n"
+ "appropriate command is not present"
+ "sik_digest is NULL"
+ "ErrorCode"
+ "HTTP send error: %!d(MISSING)\n"
+ "RePairingSessionKeyExchange"
+ "Resetting session\n"
+ "_HSCHandleMessage returned : %!d(MISSING)"
+ "SessionKeyExch"
+ "inData"
+ "%!X(MISSING)"
+ "C6"
+ "Mesa sensor serial number: %!@(MISSING)"
+ "sik_pub_key is NULL"
+ "CFDataCreate sik_digest failed"
+ "SensorSN: %!@(MISSING)"
+ "\terrorCode: "
+ "%!d(MISSING)"
+ "ApplePearlSEPDriver"
+ "Command = %!@(MISSING)\n"
+ "Output - Module Function = %!@(MISSING)\n"
+ "Request data is : %!@(MISSING)\n"
+ "Unable to relay response to SEP and obtain information \n"
+ "sendRequestSync"
+ "ApChipID"
+ "Failed to set TATSU server URL with error %!d(MISSING)"
+ "_HSCHandleMessage"
+ "useProdMasterKey"
+ "initWithBytes:length:encoding:"
+ "*replySize >= outData->dataSize"
+ "/tmp/%!@(MISSING)-from-server"
+ "ErrorCode is String Type"
+ "Exiting parse_response : %!d(MISSING)"
+ "Failed to enable single sign on"
+ "SensorSNUM"
+ "bufferSize"
+ "getModuleSerialNumber -> %!{(MISSING)errno}d\n"
+ "%!@(MISSING)\n"
+ "------- CLIENT REQUEST -------\n"
+ "Content-Length"
+ "Failed to initialize personalization manager with error %!@(MISSING)"
+ "Library-MesaFactory"
+ "POST"
+ "UUID"
+ "getApTicketForSeaCookiePairingWithOptions:pairingTicket:error:"
+ "parseResponse"
+ "PearlFactoryLib seacookie message handling."
+ "could not create contentLengthStr\n"
+ "getSensorSerialNumber %!p(MISSING) %!p(MISSING)\n"
+ "(type == kMesaFactorySeaCookieValidateTatsuTicket) || replySize"
+ "SensorSNUM: %!@(MISSING)"
+ "enableSSO:"
+ "i28@?0i8r*12Q20"
+ "Invalid Argument"
+ "Validate tatsu ticket succeeded."
+ "_HSCSeaCookieHandler"
+ "der_key_validate"
+ "pearlInfo"
+ "xmlData is not CFDictionary type."
+ "Failed to get mesa nonce with error %!@(MISSING)"
+ "Protocol Version : %!@(MISSING)"
+ "getSIKString"
+ "pearlSeaCookieHandleMessage, type=%!d(MISSING) -> 0x%!x(MISSING)\n"
+ "seaCookieHandleMessage message[%!z(MISSING)u] %!(BADPREC)%!P(MISSING)\n"
+ "HSCSecureProvisionMesaWithUIDProxy"
+ "SensorType"
+ "base64EncodedStringWithOptions:"
+ "Invalid Arguments"
+ "Unable to create Error object\n"
+ "Content-Type"
+ "Could not create proxy settings, system default proxy will be used."
+ "Failed to set SEP nonce with error %!d(MISSING)"
+ "Input argument req_dict is empty or NULL\n"
+ "Unable to get Pearl Information"
+ "/tmp/%!@(MISSING)"
+ "Create xmlData failed, error: %!@(MISSING)"
+ "Library-PearlFactory"
+ "Request"
+ "Signature = %!@(MISSING)\n"
+ "pearlSeaCookieHandleMessage, type=%!d(MISSING) reply[%!z(MISSING)u] %!(BADPREC)%!P(MISSING)\n"
+ "--------------------------------------------------------------\n"
+ "HSCGetMesaNonce"
+ "Mesa Nonce: %!@(MISSING)"
+ "mesaSensorProvisioningState"
+ "Failed to get default AMAuthInstallRef"
+ "chipID: %!u(MISSING) Size: %!l(MISSING)lu"
+ "seaCookieHandleMessage, type=%!d(MISSING) reply[%!z(MISSING)u] %!(BADPREC)%!P(MISSING)\n"
+ "v8@?0"
+ "SepNonce"
+ "Setting custom tatsu server URL: %!@(MISSING)"
+ "getModuleSerialNumber %!p(MISSING) %!p(MISSING)\n"
+ "_merge_dict_cb"
+ "numberWithInteger:"
+ "(type == kPearlFactorySeaCookieMessageS0) || (type == kPearlFactorySeaCookieGenerateNonce) || message"
+ "-[MesaPairer start]"
+ "AppleBiometricServices"
+ "Create xmlData failed."
+ "Unable to parse response data from SeaCookie server\n"
+ "Unknown SeaCookie type"
+ "XML datalen: %!l(MISSING)u data is : %!@(MISSING)\n"
+ "isSSR"
+ "------- SERVER RESPONSE -------\n"
+ "Content Length Empty"
+ "getSensorProvisioningState %!p(MISSING)\n"
+ "(type == kMesaFactorySeaCookieMessageS0) || (type == kMesaFactorySeaCookieGenerateNonce) || messageLength"
+ "/Library/Caches/com.apple.xbs/Sources/Pearl_Kernel/PearlFactoryLib/PearlFactoryLib.m"
+ "Content Length -- empty \n"
+ "Send request status: %!d(MISSING) http status: %!l(MISSING)d error: %!@(MISSING)\n"
+ "X-Apple-SeaCookie-IP"
+ "Unable to send/receive data with SeaCookie server\n"
+ "createRequestData"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) bad 2%!s(MISSING)\n"
+ "------- END CLIENT REQUEST -------\n"
+ "DataRef or responseDict is NULL."
+ "SeaCookie server returned HTTP status: %!l(MISSING)d\n"
+ "SensorChipID : %!@(MISSING)"
+ "moduleStatus = %!d(MISSING) reply[%!l(MISSING)u] \n"
+ "SensorUID: %!@(MISSING)"
+ "SpecVersion"
+ "Unable to get mesa provisioning state"
+ "service"
+ "Mesa Nonce Size: %!d(MISSING)"
+ "S5"
+ "Unknown callback type."
+ "initWithAuthInstallObj:"
+ "_HSCHandlePearlMessage"
+ "requestData : %!@(MISSING) responseData : %!@(MISSING)"
+ "SensorSN"
+ "stringWithFormat:"
+ "0x"
+ "ErrorMessage"
+ "SIK"
+ "getInnermostNSError:"
+ "AppleKeyStore"
+ "C5"
+ "_HSCHandleMesaMessage"
+ "mesaStatus: %!d(MISSING) Size: %!d(MISSING)"
+ "Not supported."
+ "mesaSensorSerialNumber"
+ "result = %!d(MISSING)\n"
+ "Processing Message  %!@(MISSING) --> %!@(MISSING)"
+ "_HSCGetMesaInfo"
+ "application/xml"
+ "numberWithUnsignedInt:"
+ "pearlSeaCookieHandleMessage %!d(MISSING) %!p(MISSING) %!z(MISSING)u %!p(MISSING) %!p(MISSING)\n"
+ "com.apple.BiometricKit"
+ "ApECID"
+ "C7"
+ "Version"
+ "_HSCPairProxy"
+ "aks"
+ "pearlStatus: %!d(MISSING) Size: %!d(MISSING)"
+ "signature"
+ "CFPropertyListCreateData failed\n"
+ "err == 0 "
+ "responseDict : %!@(MISSING)"
+ "responseDict NULL. Unable to parse Response\n"
+ "(type == kPearlFactorySeaCookieMessageS0) || (type == kPearlFactorySeaCookieGenerateNonce) || messageSize"
+ "absoluteString"
+ "could not create httpRequest\n"
+ "*bufferSize"
+ "/Library/Caches/com.apple.xbs/Sources/Mesa/AppleBiometricServices/MesaFactoryC/MesaFactoryC.c"
+ ":"
+ "PairSensor"
+ "_HSCGetModuleInfo"
+ "_aks_operation"
+ "HTTP Status == 200. OK\n"
+ "code"
+ "dataWithBytes:length:"
+ "failed to open connection to %!s(MISSING)\n"
+ "Unable to get mesa nonce"
+ "getClientAuth"
+ "00"
+ "SensorChipID"
+ "shouldPersonalizeWithSSOByDefault"
+ "S7"
+ "callback"
+ "mesaInfo"
+ "AssertMacros: %!s(MISSING) (value = 0x%!l(MISSING)x), %!s(MISSING) file: %!s(MISSING), line: %!d(MISSING)\n\n"
+ "Error is empty"
+ "Failed to create connection options dictionary.\n"
+ "getSensorSerialNumber -> %!{(MISSING)errno}d\n"
+ "mesaSensorPreviousState"
+ "startPairing"
+ "Couldn't create OS Log for 'com.apple.BiometricKit.Library-MesaFactory'!\n"
+ "Fail to provision mesa: %!i(MISSING) error: %!@(MISSING)"
+ "SensorChipID: %!@(MISSING)"
+ "_HSCGetPearlInfo"
+ "%!l(MISSING)u"
+ "CFPropertyListCreateData failed : %!@(MISSING)\n"
+ "ErrorString : %!@(MISSING)\n"
+ "SensorType : %!@(MISSING)"
+ "Calling pearl patch loading."
+ "Request Dictionary Creation failed\n"
+ "mesaModuleSerialNumber"
+ "seaCookieHandleMessage, type=%!d(MISSING) -> 0x%!x(MISSING)\n"
+ "ApChipID: %!@(MISSING)"
+ "^{__CFString=}24@?0r*8Q16"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) aks connection failed%!s(MISSING)\n"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) fail%!s(MISSING)\n"
+ "SIK : %!@(MISSING)"
+ "size == sizeof(state)"
+ "\terrorString: "
+ "Mesa Module serial number: %!@(MISSING)"
+ "Response Dictionary : %!@(MISSING)\n"
+ "S6"
+ "Server returned an "
+ "%!(BADPREC)%!s(MISSING)"
+ "C4"
+ "Unable to get Mesa Information"
+ "aksStatus is %!d(MISSING)"
+ "(type == kPearlFactorySeaCookieValidateTatsuTicket) || replySize"
+ "Unable to get current mesa provisioning state"
+ "buffer"
+ "unable to create a request \n"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) bad 1%!s(MISSING)\n"
+ "SensorNonce"
+ "SensorNonce : %!@(MISSING)"
+ "SensorUID"
+ "_HSCHandleMessage Failed"
+ "ErrorMessage - %!@(MISSING)"
+ "IOService:/IOResources/AppleKeyStore"
+ "SERVER RESPONSE is NULL\n"
+ "development-cert"
+ "inputData --> %!@(MISSING) inputSize --> %!l(MISSING)u"
+ "(type == kPearlFactorySeaCookieValidateTatsuTicket) || reply"
+ "inputData"
+ "Session"
+ "cmd"
+ "(type == kMesaFactorySeaCookieMessageS0) || (type == kMesaFactorySeaCookieGenerateNonce) || message"
+ "Couldn't create OS Log for 'com.apple.BiometricKit.Library-PearlFactory'!\n"
+ "Failed to create timeout\n"
+ "Payload = %!@(MISSING)\n"
+ "SepNonce : %!@(MISSING)"
+ "Server did not return session cookie"
+ "createError"
+ "xmlData : %!@(MISSING)"
+ "Command"
+ "MesaFactoryC seacookie message handling."
+ "TrustedAccessoryFactory seacookie message handling."
+ "i"
+ "Disabling SSL validation"
+ "ReprovisionSensor"
+ "getSensorProvisioningState -> %!{(MISSING)errno}d %!d(MISSING)\n"
+ "1.2"
+ "Failed to create max attempts\n"
+ "aks-client-queue"
+ "getDefaultAMAuthInstallRef"

```
