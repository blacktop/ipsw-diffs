## com.apple.MEValidationService

> `/System/Library/Frameworks/MediaExtension.framework/Versions/Current/XPCServices/com.apple.MEValidationService.xpc/Contents/MacOS/com.apple.MEValidationService`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`

```diff

-3350.71.2.0.0
-  __TEXT.__text: 0x1e70
-  __TEXT.__auth_stubs: 0x530
+3350.77.5.6.0
+  __TEXT.__text: 0x10b4
+  __TEXT.__auth_stubs: 0x510
   __TEXT.__objc_stubs: 0xe0
-  __TEXT.__const: 0x48
+  __TEXT.__const: 0x10
   __TEXT.__cstring: 0x552
-  __TEXT.__oslogstring: 0x1020
+  __TEXT.__oslogstring: 0x15b
   __TEXT.__objc_methname: 0x82
-  __TEXT.__unwind_info: 0x98
+  __TEXT.__unwind_info: 0x90
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x2a0
-  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_selrefs: 0x38
   __DATA.__bss: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 12
-  Symbols:   108
-  CStrings:  83
+  Symbols:   103
+  CStrings:  31
 
Symbols:
- _CFAbsoluteTimeGetCurrent
- __xpc_error_connection_invalid
- __xpc_error_key_description
- __xpc_error_termination_imminent
- _strerror
CStrings:
- "Access denied for path = %s, an error occurred: %{public}s (%d)."
- "Access denied for path = %{public}s, the operation is not allowed."
- "CheckHostApplicationHasRequiredSandboxAccess: unable to obtain path chars from string"
- "CheckHostApplicationHasRequiredSandboxAccess: unable to obtain path string from URL"
- "CopyAndValidateBundlePlistDictionary: Info.plist is missing or invalid"
- "CopyAndValidateBundlePlistDictionary: SecCodeCheckValidityWithErrors failed with error : (%d)(%@) "
- "CopyAndValidateBundlePlistDictionary: SecCodeCreateWithAuditToken failed with error : %d"
- "CopyAndValidateBundlePlistDictionary: SecRequirementCreateWithString failed with error : %d"
- "CopyAndValidateBundlePlistDictionary: missing App Sandbox entitlement"
- "CopyAndValidateBundlePlistDictionary: missing format reader entitlement "
- "CopyAndValidateBundlePlistDictionary: read of code signing info failed with error %d"
- "CopyAndValidateBundlePlistDictionary: unable to read entitlements"
- "CopyFileURLFromOpenFileDescriptor: unable to obtain URL from file descriptor"
- "CopyFileURLFromOpenFileDescriptor: unable to obtain path from file descriptor"
- "CreateFileExtensionsSetFromBundlePlist: Denied media extension control over file name extension %@"
- "CreateFileExtensionsSetFromBundlePlist: Unable to obtain set of file extensions to deny"
- "CreateFileExtensionsSetFromBundlePlist: format reader bundle contains invalid extensions"
- "CreateFileExtensionsSetFromBundlePlist: unable to create lower case extension string"
- "CreateRelativeDirectoryEnumeration: CFURLEnumeratorGetNextURL failed with error code %lld"
- "CreateRelativeDirectoryEnumeration: unable to create directory enumerator"
- "CreateRelativeDirectoryEnumeration: unexpected result from CFURLEnumeratorGetNextURL"
- "MEValidationService: DISABLED -- Exiting."
- "MEValidationService: Host application is denied read-access to related files"
- "MEValidationService: Unable to obtain source file URL from XPC file descriptor"
- "MEValidationService: Unable to obtain source file directory URL"
- "MEValidationService: XPC error %s"
- "MEValidationService: XPC termination imminent"
- "MEValidationService: XPCConnectionHandler started"
- "MEValidationService: got request for relative file names"
- "MEValidationService: got request to open file descriptor"
- "MEValidationService: invalid XPC message object"
- "MEValidationService: invalid file descriptor in XPC request"
- "MEValidationService: peer connection has gone invalid; exiting"
- "MEValidationService: reply message sent"
- "MEValidationService: request does not originate from an extension format reader"
- "MEValidationService: sandbox_init_with_parameters err:%d errorbuf:%s -- Exiting."
- "MEValidationService: starting up .... "
- "RequestRelativeFilenames: allowed file list is NULL"
- "RequestRelativeFilenames: file %@ has a file extension from deny-list"
- "RequestRelativeFilenames: unable to create set of valid file extensions"
- "RequestRelativeFilenames: unable to obtain plist dictionary for bundle"
- "RequestToOpenAuxiliaryFileDescriptor: file %@ has a file extension from deny-list"
- "RequestToOpenAuxiliaryFileDescriptor: invalid relative file name string"
- "RequestToOpenAuxiliaryFileDescriptor: requested file extension is not in allowed list"
- "RequestToOpenAuxiliaryFileDescriptor: unable to create auxiliary file URL"
- "RequestToOpenAuxiliaryFileDescriptor: unable to create auxiliary file path CFString"
- "RequestToOpenAuxiliaryFileDescriptor: unable to create set of valid file extensions"
- "RequestToOpenAuxiliaryFileDescriptor: unable to make CFString for name of file to open"
- "RequestToOpenAuxiliaryFileDescriptor: unable to obtain name of file to open"
- "RequestToOpenAuxiliaryFileDescriptor: unable to obtain plist dictionary for bundle"
- "RequestToOpenAuxiliaryFileDescriptor: unable to open auxiliary file path, errno = %d"
- "RequestToOpenAuxiliaryFileDescriptor: unable to store auxiliary file path"
```
