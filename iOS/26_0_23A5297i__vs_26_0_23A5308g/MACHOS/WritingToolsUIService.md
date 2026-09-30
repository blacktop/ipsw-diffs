## WritingToolsUIService

> `/Applications/WritingToolsUIService.app/WritingToolsUIService`

```diff

-79.100.0.0.0
-  __TEXT.__text: 0x1b4d64
-  __TEXT.__auth_stubs: 0x5560
+82.1.0.0.0
+  __TEXT.__text: 0x1b6f34
+  __TEXT.__auth_stubs: 0x5550
   __TEXT.__objc_methlist: 0x1264
-  __TEXT.__const: 0x10b84
-  __TEXT.__cstring: 0x894a
-  __TEXT.__swift5_typeref: 0x2e380
-  __TEXT.__constg_swiftt: 0x6634
-  __TEXT.__objc_methname: 0x4286
+  __TEXT.__const: 0x10bd4
+  __TEXT.__cstring: 0x840a
+  __TEXT.__swift5_typeref: 0x2e494
+  __TEXT.__constg_swiftt: 0x6628
+  __TEXT.__objc_methname: 0x42a4
   __TEXT.__swift5_reflstr: 0x3b81
   __TEXT.__swift5_fieldmd: 0x3a4c
   __TEXT.__swift5_builtin: 0x1f4

   __TEXT.__swift5_proto: 0x71c
   __TEXT.__swift5_types: 0x42c
   __TEXT.__objc_classname: 0x240
-  __TEXT.__objc_methtype: 0x1b12
-  __TEXT.__oslogstring: 0x3f7b
-  __TEXT.__swift5_capture: 0x1b78
-  __TEXT.__swift_as_entry: 0x1cc
-  __TEXT.__swift_as_ret: 0x210
+  __TEXT.__objc_methtype: 0x1b2f
+  __TEXT.__oslogstring: 0x40fb
+  __TEXT.__swift5_capture: 0x1bc8
+  __TEXT.__swift_as_entry: 0x1d0
+  __TEXT.__swift_as_ret: 0x214
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x55c8
-  __TEXT.__eh_frame: 0x6fa0
-  __DATA_CONST.__auth_got: 0x2ab0
+  __TEXT.__unwind_info: 0x55e0
+  __TEXT.__eh_frame: 0x7000
+  __DATA_CONST.__auth_got: 0x2aa8
   __DATA_CONST.__got: 0x1510
   __DATA_CONST.__auth_ptr: 0x1cb0
-  __DATA_CONST.__const: 0x9b98
+  __DATA_CONST.__const: 0x9c90
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0x3ba8
   __DATA.__objc_selrefs: 0x1148
   __DATA.__objc_data: 0x18d0
-  __DATA.__data: 0xdde0
+  __DATA.__data: 0xde80
   __DATA.__bss: 0xf010
-  __DATA.__common: 0x748
+  __DATA.__common: 0x758
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 921C3AA2-FD01-3D91-915F-EFA772E5D804
-  Functions: 7691
+  UUID: 1BB314A1-5E68-3096-A517-75C2430B0AE0
+  Functions: 7713
   Symbols:   2570
-  CStrings:  1794
+  CStrings:  1782
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
- _$s14WritingToolsUI16WTStartupOptionsC6promptSSSgvgTj
CStrings:
+ "@\"UIWindow\""
+ "@\"WTSession\""
+ "Handoff approved, proceeding..."
+ "Handoff state changed, request alert presentation"
+ "Initiating handoff to UCB... (enrolled: %{bool}d)"
+ "Proceeding with partner handoff"
+ "Received enrollment dimissal completion, sending handoff"
+ "Received enrollment dismissed result: %{bool}d"
+ "Requested full screen presentation without a mode specified!"
+ "Requesting enrollment prior to partner handoff..."
+ "User did not enroll, ending writing tools"
+ "` tool.\n    - Some examples of missing information that might be needed from the user:\n        - **For a resume**:\n            - Personal details, e.g. name, address, phone number, email, LinkedIn profile\n            - Objective statement\n            - Work experience, e.g. job titles, company names, locations, dates, responsibilities, achievements\n            - Education, e.g. degrees, universities, locations, graduation dates, relevant coursework, academic achievements\n            - Skills\n            - Certifications\n            - Professional development, e.g. courses, conferences attended\n        - **For an event invitation**:\n            - Event name\n            - Host details, e.g. name, contact info\n            - Guest list\n            - Date and time\n            - Location\n            - Event agenda or activities\n            - RSVP details\n        - **For a review**:\n            - Name of the place or event, e.g. restaurant, movie, theme park\n            - Date of visit or event\n            - Specific experiences, e.g dishes ordered, favorite parts, criticisms\n            - Ratings, e.g. service quality, overall experience\n            - Additional comments or recommendations\n2. If the document is missing critical information, return the information you are requesting from the user in the `requestedInfo` field of the output object. Each request should include:\n    - `name`: The unique, human-readable identifier of the requested information. Examples:\n        - Email address\n        - Home address\n        - Restaurant name\n        - Rating\n\n*Important*: Only call the "
+ "actionForEnrollmentDismissedWithCompletion:"
+ "enrollmentDismissedWithCompletion:"
+ "updateKeyboardTrackingHeight, sending %f"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?>16"
- "Handling handoff to UCB..."
- "How was the quality of service at the restaurant I went to last night?"
- "Not yet enrolled"
- "Proceeding with handoff"
- "What are the important points of the letter to my vendor?"
- "What did I rate Six Flags out of 10?"
- "What did I rate he movie from last week out of 5 stars?"
- "What dishes did I at the restaurant I went to last night?"
- "What is my contact info?"
- "What is my name?"
- "What is my sister's contact info?"
- "What is my son's contact info?"
- "What is my vendor's contact info?"
- "What is the reason for the thank you message?"
- "What is the recipient's name?"
- "What should the subject of the letter to my vendor be?"
- "What was the ticket prize for Six Flags?"
- "What were my biggest criticisms of the movie I watched last week?"
- "What were my favorite parts of the movie I watched last week?"
- "What were my favorite rides at Six Flags?"
- "What's my contact info?"
- "When and where is my son's birthday party?"
- "When did I last go to Six Flags?"
- "Which movie did I watch last week?"
- "Which restaurant did I go to last night?"
- "` tool.\n    - Some examples of missing information that might be needed from the user:\n        - **For a resume**:\n            - Personal details, e.g. name, address, phone number, email, LinkedIn profile\n            - Objective statement\n            - Work experience, e.g. job titles, company names, locations, dates, responsibilities, achievements\n            - Education, e.g. degrees, universities, locations, graduation dates, relevant coursework, academic achievements\n            - Skills\n            - Certifications\n            - Professional development, e.g. courses, conferences attended\n        - **For an event invitation**:\n            - Event name\n            - Host details, e.g. name, contact info\n            - Guest list\n            - Date and time\n            - Location\n            - Event agenda or activities\n            - RSVP details\n        - **For a review**:\n            - Name of the place or event, e.g. restaurant, movie, theme park\n            - Date of visit or event\n            - Specific experiences, e.g dishes ordered, favorite parts, criticisms\n            - Ratings, e.g. service quality, overall experience\n            - Additional comments or recommendations\n2. If the document is missing critical information, return the information you are requesting from the user in the `requestedInfo` field of the output object. Each request should include:\n    - `name`: The unique, human-readable identifier of the requested information. Examples:\n        - Email address\n        - Home address\n        - Restaurant name\n        - Rating\n    - `query`: A short natural language query that will be used to retrieve the information on the user's device. Use the first person. Examples:\n        - Calendar event for restaurant reservation\n        - Sister's email address\n        - My work phone number\n\n*Important*: Only call the "
- "actionForEnrollmentDismissed"
- "enrollmentDismissed"
- "updateKeyboardTrackingHeight, sendinging %f"

```
