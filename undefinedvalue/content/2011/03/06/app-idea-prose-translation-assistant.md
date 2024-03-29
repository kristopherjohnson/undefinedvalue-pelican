Title: App Idea: Prose Translation Assistant
Date: 2011-03-07 02:03:21
Category: Blog
Slug: app-idea-prose-translation-assistant
Alias: 2011/03/06/app-idea-prose-translation-assistant/
Tags: idea


(This is just an _idea_. As I explain my post about [Why I Loved The Social Network](https://undefinedvalue.com/2011/02/26/why-i-loved-social-network), I think ideas are cheap, so if you want to "steal" this idea and make the app, I heartily support you.)

A friend has started a personal project to translate the works of Jules Verne from the original French into English, as he is dissatisfied with the existing English translations. He is going about it pretty much the way I would: he has a browser window open with the original French text, a browser window with Google Translate, and a text editor where he is writing the English translation. He also has a French-English dictionary on hand.

I wondered whether there might be some software available that is specifically designed for this purpose. Some Googling finds plenty of applications to assist in translation, but all the ones I found are designed to help translate conversations, e-mails, or other such things. I couldn't find anything designed for assisting with translating a novel, play, or other such work, where the translation needs to be written by a human in an accurate-but-artful way.

It got me thinking about how I would design an application to assist with this process, making it less necessary to switch between various applications and documents.
<!--break-->
The basic presentation in my mind is a table with three columns: the first column contains the original text, the second column contains the text translated into the target language, and the third column is intended to hold notes. There would be a button and simple keyboard shortcut for showing/hiding the third column.

There would be one paragraph per row. So, the main window would look something like this:

<table border="1">
<tr>
<th> P# </th>
<th>French</th>
<th>English</th>
<th>Notes</th>
</tr>

<tr>
<td>1</td>
<td>

L'année 1866 fut marquée par un événement bizarre, un phénomène inexpliqué et inexplicable que personne n'a sans doute oublié. Sans parler des rumeurs qui agitaient les populations des ports et surexcitaient l'esprit public à l'intérieur des continents les gens de mer furent particulièrement émus. Les négociants, armateurs, capitaines de navires, skippers et masters de l'Europe et de l'Amérique, officiers des marines militaires de tous pays, et, après eux, les gouvernements des divers États des deux continents, se préoccupèrent de ce fait au plus haut point.

</td>

<td>

The year 1866 was marked by a bizarre development, an unexplained and downright inexplicable phenomenon that surely no one has forgotten. Without getting into those rumors that upset civilians in the seaports and deranged the public mind even far inland, it must be said that professional seamen were especially alarmed. Traders, shipowners, captains of vessels, skippers, and master mariners from Europe and America, naval officers from every country, and at their heels the various national governments on these two continents, were all extremely disturbed by the business.

</td>

<td>

Does the English word "downright" in the first sentence capture the correct meaning?

</td>

</tr>
<td>2</td>
<td>

En effet, depuis quelque temps, plusieurs navires s'étaient rencontrés sur mer avec « une chose énorme » un objet long, fusiforme, parfois phosphorescent, infiniment plus vaste et plus rapide qu'une baleine.

</td>

<td>

In essence, over a period of time several ships had encountered "an enormous thing" at sea, a long spindle–shaped object, sometimes giving off a phosphorescent glow, infinitely bigger and faster than any whale.

</td>

<td>

&nbsp;

</td>
</tr>

<tr>
<td>3</td>
<td>

Les faits relatifs à cette apparition, consignés aux divers livres de bord, s'accordaient assez exactement sur la structure de l'objet ou de l'être en question, la vitesse inouïe de ses mouvements, la puissance surprenante de sa locomotion, la vie particulière dont il semblait doué. Si c'était un cétacé, il surpassait en volume tous ceux que la science avait classés jusqu'alors. Ni Cuvier, ni Lacépède, ni M. Dumeril, ni M. de Quatrefages n'eussent admis l'existence d'un tel monstre — à moins de l'avoir vu, ce qui s'appelle vu de leurs propres yeux de savants.

</td>
<td>

The facts concerning this apparition, as recorded in various logbooks, agreed pretty accurately the structure of the object or creature in question, the unprecedented speed of its movements, the surprising power of locomotion, life which he seemed particularly gifted. If it was a cetacean, it surpassed in size all that science had previously ordered. Neither Cuvier, Lacepede neither nor Mr. Dumeril nor M. de Quatre had not admitted the existence of such a monster - at least to have seen, which is called saw with their own eyes of scholars.

</td>

<td>

(Automatic translation by Google Translate.)

</td>
</tr>
</table>

There would then be a set of floating auxiliary windows that provide assistance. For example, a Google Translate window would appear which displays translated text. By default, it would display a translation of the current paragraph, but if one or more words were selected, then it would display the translation for only the selected word/phrase/sentence. There would also be a Babelfish window, a window with a dictionary for the target language, and windows for any other sources of translation assistance.

When you create a new translation project, you would import the original-language text, and could also then import a translation, or could allow the application to automatically generate an initial translation using Google Translate or another service.

I am assuming that _paragraph_ is the best chunk size for this kind of work. I think a sentence is too short, as it is likely one would want to split or combine sentences when writing a nicely flowing translation. A chapter is too long to be an atomic unit, but there should be a way to create some sort of outline view to show and hide larger groups of paragraphs. (Are there written languages that don't have a concept analogous to a _paragraph_?)

Each paragraph can be marked with a color to indicate its status: _unedited initial translation_, _edited but incomplete_, _needs review_, or _finished_.

There needs to be an easy way to share the project with others, and merge others' work into your own. (Maybe one more column for each additional author?)

I'm not sure whether this should be a desktop app or a web app. A web app would make it easier to share work between people and let people review it, so that's probably the way to go.

Anyway, that's the idea. It's too much work for me to try to tackle, but maybe somebody else wants to try, or can point me to existing examples of this type of product.
