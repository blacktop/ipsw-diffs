## AppIntentSchemas

> `FileSystem/System/Library/PrivateFrameworks/AppIntentSchemas.framework/Localizable.loctable`

```diff

 en.browser_BookmarkTabIntent_1.0.0_intent_parameter_name_title = "Title"
 en.browser_BookmarkTabIntent_1.0.0_intent_parameter_tab_description = "Tab to bookmark."
 en.browser_BookmarkTabIntent_1.0.0_intent_parameter_tab_title = "Tab"
+en.browser_BookmarkTabIntent_1.0.0_intent_side_effect_confirmation_template_0 = "Do you want to bookmark ${tab} as ${name} in ${applicationName}?"
+en.browser_BookmarkTabIntent_1.0.0_intent_side_effect_confirmation_template_1 = "Do you want to bookmark ${tab} in ${applicationName}?"
 en.browser_BookmarkTabIntent_1.0.0_intent_template_parameter_summary_0 = "Bookmark ${tab}"
 en.browser_BookmarkTabIntent_1.0.0_intent_title = "Bookmark Tab"
 en.browser_BookmarkURLIntent_1.0.0_intent_description = "Creates a new bookmark for a given URL."

 en.browser_BookmarkURLIntent_1.0.0_intent_parameter_name_title = "Name"
 en.browser_BookmarkURLIntent_1.0.0_intent_parameter_url_description = "URL to bookmark."
 en.browser_BookmarkURLIntent_1.0.0_intent_parameter_url_title = "URL"
+en.browser_BookmarkURLIntent_1.0.0_intent_side_effect_confirmation_template_0 = "Do you want to bookmark ${url} as ${name} in ${applicationName}?"
+en.browser_BookmarkURLIntent_1.0.0_intent_side_effect_confirmation_template_1 = "Do you want to bookmark ${url} in ${applicationName}?"
 en.browser_BookmarkURLIntent_1.0.0_intent_template_parameter_summary_0 = "Bookmark ${url}"
 en.browser_BookmarkURLIntent_1.0.0_intent_title = "Bookmark URL"
 en.browser_BrowserTabContent_1.0.0_union_type_display_representation = "Contents"

 en.browser_CloseTabsIntent_1.0.0_intent_description = "Closes the selected tabs."
 en.browser_CloseTabsIntent_1.0.0_intent_parameter_target_description = "Tabs to close."
 en.browser_CloseTabsIntent_1.0.0_intent_parameter_target_title = "Tabs"
+en.browser_CloseTabsIntent_1.0.0_intent_side_effect_confirmation_button_cancel = "Cancel"
+en.browser_CloseTabsIntent_1.0.0_intent_side_effect_confirmation_button_confirm = "Close"
+en.browser_CloseTabsIntent_1.0.0_intent_side_effect_confirmation_template_0 = "Do you want to close ^[${target#count} tab](inflect: true) in ${applicationName}?"
+en.browser_CloseTabsIntent_1.0.0_intent_side_effect_confirmation_template_supporting_0 = "Close ^[${target#count} tab](inflect: true)?"
 en.browser_CloseTabsIntent_1.0.0_intent_template_parameter_summary_0 = "Close ${target}"
 en.browser_CloseTabsIntent_1.0.0_intent_title = "Close Tabs"
 en.browser_CloseWindowsIntent_1.0.0_intent_description = "Closes the selected windows."
 en.browser_CloseWindowsIntent_1.0.0_intent_parameter_target_description = "Windows to close."
 en.browser_CloseWindowsIntent_1.0.0_intent_parameter_target_title = "Windows"
+en.browser_CloseWindowsIntent_1.0.0_intent_side_effect_confirmation_button_cancel = "Cancel"
+en.browser_CloseWindowsIntent_1.0.0_intent_side_effect_confirmation_button_confirm = "Close"
+en.browser_CloseWindowsIntent_1.0.0_intent_side_effect_confirmation_template_0 = "Do you want to close ^[${target#count} window](inflect: true) in ${applicationName}?"
+en.browser_CloseWindowsIntent_1.0.0_intent_side_effect_confirmation_template_supporting_0 = "Close ^[${target#count} window](inflect: true)?"
 en.browser_CloseWindowsIntent_1.0.0_intent_template_parameter_summary_0 = "Close ${target}"
 en.browser_CloseWindowsIntent_1.0.0_intent_title = "Close Windows"
 en.browser_CreateTabIntent_1.0.0_intent_description = "Creates a new tab with a URL loaded, or blank if omitted."

 en.browser_DeleteBookmarksIntent_1.0.0_intent_description = "Deletes the selected bookmarks."
 en.browser_DeleteBookmarksIntent_1.0.0_intent_parameter_entities_description = "Bookmarks to delete."
 en.browser_DeleteBookmarksIntent_1.0.0_intent_parameter_entities_title = "Bookmarks"
+en.browser_DeleteBookmarksIntent_1.0.0_intent_side_effect_confirmation_button_cancel = "Cancel"
+en.browser_DeleteBookmarksIntent_1.0.0_intent_side_effect_confirmation_button_confirm = "Delete"
+en.browser_DeleteBookmarksIntent_1.0.0_intent_side_effect_confirmation_template_0 = "Do you want to delete ^[${entities#count} bookmark](inflect: true) from ${applicationName}?"
+en.browser_DeleteBookmarksIntent_1.0.0_intent_side_effect_confirmation_template_supporting_0 = "Delete ^[${entities#count} bookmark](inflect: true)?"
 en.browser_DeleteBookmarksIntent_1.0.0_intent_template_parameter_summary_0 = "Delete ${entities}"
 en.browser_DeleteBookmarksIntent_1.0.0_intent_title = "Delete Bookmarks"
 en.browser_FindOnPageIntent_1.0.0_intent_description = "Find the given text on the selected tab."

```
