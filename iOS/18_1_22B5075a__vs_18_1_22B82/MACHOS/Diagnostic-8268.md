## Diagnostic-8268

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8268.appex/Diagnostic-8268`

```diff

-645.42.1.0.0
-  __TEXT.__text: 0x293c
-  __TEXT.__auth_stubs: 0x250
-  __TEXT.__objc_stubs: 0x300
-  __TEXT.__objc_methlist: 0x10c
-  __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x31e
-  __TEXT.__oslogstring: 0x2c0
+645.42.2.0.0
+  __TEXT.__text: 0xb7e4
+  __TEXT.__auth_stubs: 0x770
+  __TEXT.__objc_stubs: 0x6a0
+  __TEXT.__objc_methlist: 0x124
+  __TEXT.__const: 0xc0
+  __TEXT.__cstring: 0x17bb
+  __TEXT.__oslogstring: 0x93e
   __TEXT.__objc_classname: 0x3c
-  __TEXT.__objc_methname: 0x57a
-  __TEXT.__objc_methtype: 0x13e
-  __TEXT.__unwind_info: 0xb0
-  __DATA_CONST.__auth_got: 0x130
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x80
-  __DATA_CONST.__cfstring: 0x280
+  __TEXT.__objc_methname: 0x74f
+  __TEXT.__objc_methtype: 0x159
+  __TEXT.__unwind_info: 0x148
+  __DATA_CONST.__auth_got: 0x3c0
+  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0x170
+  __DATA_CONST.__cfstring: 0xe60
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__objc_classrefs: 0x8
+  __DATA_CONST.__objc_intobj: 0x120
   __DATA.__objc_const: 0x670
-  __DATA.__objc_selrefs: 0x128
+  __DATA.__objc_selrefs: 0x1d8
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0xc0
-  __DATA.__bss: 0x18
-  __DATA.__common: 0x18
+  __DATA.__data: 0x184
+  __DATA.__bss: 0x48
+  __DATA.__common: 0x28
+  - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 35
-  Symbols:   64
-  CStrings:  176
+  Functions: 115
+  Symbols:   180
+  CStrings:  466
 
Symbols:
+ _AMAuthInstallApImg4SetSepNonce
+ _AMAuthInstallSetSigningServerURL
+ _AMFDRCreateTypeWithOptions
+ _AMFDRDataCopy
+ _AMFDRDataCopyTrustObject
+ _AMFDRDataCreatePermissionsString
+ _AMFDRPermissionsRequest
+ _AMFDRSealingMapCopyInstanceForClass
+ _AMFDRSealingMapGetFDRDataVersionForDevice
+ _AMFDRSetOption
+ _AMSupportCopyHexStringFromData
+ _AMSupportCreateSetFromCFIndexArray
+ _AMSupportHttpCopyProxySettings
+ _AMSupportHttpSendSync
+ _AMSupportLogDumpMemory
+ _AMSupportLogInternal
+ _AMSupportLogSetHandler
+ _AMSupportSafeRelease
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
+ _CFHTTPMessageCopyAllHeaderFields
+ _CFHTTPMessageCreateRequest
+ _CFHTTPMessageSetBody
+ _CFHTTPMessageSetHeaderFieldValue
+ _CFNumberCreate
+ _CFPropertyListCreateData
+ _CFPropertyListCreateWithData
+ _CFRelease
+ _CFRetain
+ _CFStringAppend
+ _CFStringCompare
+ _CFStringCreateMutable
+ _CFStringCreateMutableCopy
+ _CFStringCreateWithFormat
+ _CFStringGetTypeID
+ _CFUUIDCreate
+ _CFUUIDCreateString
+ _CRErrorDomain
+ _HSCGetMesaNonce
+ _HSCSecureProvisionMesaWithUID
+ _HSCSecureProvisionMesaWithUIDProxy
+ _IOConnectCallMethod
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryFromPath
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_CRPersonalizationManager
+ _OBJC_CLASS_$_CRPreflightController
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSString
+ __NSConcreteStackBlock
+ ___chkstk_darwin
+ ___osLogPearlLib
+ ___osLogPearlLibTrace
+ ___stderrp
+ ___stdoutp
+ __logHandler
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
+ _dispatch_queue_create
+ _dispatch_sync
+ _fprintf
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
+ _malloc
+ _malloc_type_calloc
+ _memcmp
+ _memcpy
+ _memset_s
+ _objc_autorelease
+ _objc_release
+ _objc_release_x28
+ _objc_retainAutorelease
+ _objc_retainAutoreleasedReturnValue
+ _objc_retainBlock
+ _pearlSeaCookieHandleMessage
+ _qsort
+ _syslog
CStrings:
+ "\terrorCode: "
+ "\terrorString: "
+ "%!(BADPREC)%!s(MISSING)"
+ "%!X(MISSING)"
+ "%!@(MISSING)"
+ "%!@(MISSING)\n"
+ "%!d(MISSING)"
+ "%!l(MISSING)u"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) aks connection failed%!s(MISSING)\n"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) bad 1%!s(MISSING)\n"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) bad 2%!s(MISSING)\n"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) fail%!s(MISSING)\n"
+ "(type == kMesaFactorySeaCookieMessageS0) || (type == kMesaFactorySeaCookieGenerateNonce) || message"
+ "(type == kMesaFactorySeaCookieMessageS0) || (type == kMesaFactorySeaCookieGenerateNonce) || messageLength"
+ "(type == kMesaFactorySeaCookieValidateTatsuTicket) || reply"
+ "(type == kMesaFactorySeaCookieValidateTatsuTicket) || replySize"
+ "(type == kPearlFactorySeaCookieMessageS0) || (type == kPearlFactorySeaCookieGenerateNonce) || message"
+ "(type == kPearlFactorySeaCookieMessageS0) || (type == kPearlFactorySeaCookieGenerateNonce) || messageSize"
+ "(type == kPearlFactorySeaCookieValidateTatsuTicket) || reply"
+ "(type == kPearlFactorySeaCookieValidateTatsuTicket) || replySize"
+ "*bufferSize"
+ "*replySize >= outData->dataSize"
+ "------- CLIENT REQUEST -------\n"
+ "------- END CLIENT REQUEST -------\n"
+ "------- END SERVER RESPONSE -------\n"
+ "------- SERVER RESPONSE -------\n"
+ "--------------------------------------------------------------\n"
+ "-[MesaPairer start]"
+ "-[MesaPairer verifyMSRkWithError:]"
+ "/Library/Caches/com.apple.xbs/Sources/Pearl_Kernel/PearlFactoryLib/PearlFactoryLib.m"
+ "/tmp/%!@(MISSING)"
+ "/tmp/%!@(MISSING)-from-server"
+ "00"
+ "0x"
+ "1.2"
+ ":"
+ "ApChipID"
+ "ApChipID: %!@(MISSING)"
+ "ApECID"
+ "ApECID: %!@(MISSING)"
+ "AppleKeyStore"
+ "ApplePearlSEPDriver"
+ "B32@0:8@16^@24"
+ "C4"
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
+ "Failed to create AMFDRRemote object"
+ "Failed to create connection options dictionary.\n"
+ "Failed to create max attempts\n"
+ "Failed to create timeout\n"
+ "Failed to enable single sign on"
+ "Failed to get Mesa state: 0x%!x(MISSING)"
+ "Failed to get data instance, error: %!@(MISSING)"
+ "Failed to get default AMAuthInstallRef"
+ "Failed to get mesa nonce with error %!@(MISSING)"
+ "Failed to get remote data class, error: %!@(MISSING)"
+ "Failed to initialize personalization manager with error %!@(MISSING)"
+ "Failed to load data: 0x%!x(MISSING)"
+ "Failed to load remote dataclass"
+ "Failed to request FDR Permissions: %!@(MISSING)"
+ "Failed to set SEP nonce with error %!d(MISSING)"
+ "Failed to set TATSU server URL with error %!d(MISSING)"
+ "Failed to verify MSRk %!@(MISSING)"
+ "Get remote data"
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
+ "Library-PearlFactory"
+ "Load remote data"
+ "Local"
+ "MSRk"
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
+ "Permissions"
+ "Physical presence not reset"
+ "Processing Message  %!@(MISSING) --> %!@(MISSING)"
+ "Protocol Version : %!@(MISSING)"
+ "RePairingSessionKeyExchange"
+ "Remote"
+ "ReprovisionSensor"
+ "Request"
+ "Request Dictionary Creation failed\n"
+ "Request FDR permissionStr: %!@(MISSING)"
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
+ "SensorChipID : %!@(MISSING)"
+ "SensorChipID: %!@(MISSING)"
+ "SensorNonce"
+ "SensorNonce : %!@(MISSING)"
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
+ "Signature = %!@(MISSING)\n"
+ "SpecVersion"
+ "TrustObject"
+ "TrustedAccessoryFactory seacookie message handling."
+ "UNIMPLEMENTED - mesaSetFDRData type:%!d(MISSING) data:%!p(MISSING) dataLength:%!z(MISSING)u\n"
+ "UUID"
+ "Unable to create Error object\n"
+ "Unable to create permission string for getting remote data"
+ "Unable to get Mesa Information"
+ "Unable to get Pearl Information"
+ "Unable to get current mesa provisioning state"
+ "Unable to get mesa nonce"
+ "Unable to get mesa provisioning state"
+ "Unable to get mesa serial number"
+ "Unable to parse response data from SeaCookie server\n"
+ "Unable to receive Module Information\n"
+ "Unable to relay response to SEP and obtain information \n"
+ "Unable to send/receive data with SeaCookie server\n"
+ "Unable to validate tatsu ticket"
+ "Unexpected Mesa state: %!d(MISSING)"
+ "Unknown SeaCookie type"
+ "Unknown callback type."
+ "Validate tatsu ticket succeeded."
+ "Verify successfully"
+ "Version"
+ "X-Apple-SeaCookie-IP"
+ "XML datalen: %!l(MISSING)u data is : %!@(MISSING)\n"
+ "^{__CFString=}24@?0r*8Q16"
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
+ "_aks_operation"
+ "_merge_dict_cb"
+ "absoluteString"
+ "aks"
+ "aks-client-queue"
+ "aksStatus is %!d(MISSING)"
+ "application/xml"
+ "appropriate command is not present"
+ "base64EncodedStringWithOptions:"
+ "buffer"
+ "bufferSize"
+ "bytes"
+ "callback"
+ "chipID: %!u(MISSING) Size: %!l(MISSING)lu"
+ "code"
+ "could not create contentLengthStr\n"
+ "could not create httpRequest\n"
+ "createError"
+ "createRequestData"
+ "dataWithBytes:length:"
+ "der_key_validate"
+ "development-cert"
+ "enableSSO:"
+ "errorWithDomain:code:userInfo:"
+ "failed to open connection to %!s(MISSING)\n"
+ "getApTicketForSeaCookiePairingWithOptions:pairingTicket:error:"
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
+ "getSensorSerialNumber, retry: %!d(MISSING)\n"
+ "i"
+ "i28@?0i8r*12Q20"
+ "inData"
+ "initWithAuthInstallObj:"
+ "initWithBytes:length:encoding:"
+ "inputData"
+ "inputData --> %!@(MISSING) inputSize --> %!l(MISSING)u"
+ "isSSR"
+ "length"
+ "loadMSRkWithData:error:"
+ "localizedDescription"
+ "mesaInfo"
+ "mesaModuleSerialNumber"
+ "mesaSensorPreviousState"
+ "mesaSensorProvisioningState"
+ "mesaSensorSerialNumber"
+ "mesaSetFDRData type:%!d(MISSING) data:%!p(MISSING) dataLength:%!z(MISSING)u\n"
+ "mesaSetFDRData, type=%!d(MISSING) -> 0x%!x(MISSING)\n"
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
+ "q24@0:8^@16"
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
+ "shouldPersonalizeWithSSOByDefault"
+ "sign:keyBlob:"
+ "signature"
+ "sik_digest is NULL"
+ "sik_pub_key is NULL"
+ "sik_pub_key_len is 0"
+ "startPairing"
+ "stringWithFormat:"
+ "unable to create a request \n"
+ "useProdMasterKey"
+ "verifyMSRkWithError:"
+ "xmlData : %!@(MISSING)"
+ "xmlData is not CFDictionary type."

```
