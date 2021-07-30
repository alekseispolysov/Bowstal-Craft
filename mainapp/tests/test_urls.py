from django.test import SimpleTestCase
from django.urls import reverse, resolve
from mainapp.views import HomePage, NewsPage, NewsAllPage, PostDetailPage, AboutPage, SupportUs, DownloadPage, ContactPage, ConfirmPage, SecurityContactPage, SuccessSecurityPage

# testing the whole url tree from urls.py on resolving the right view function

# how to unit test a classbased view in here by url
class TestUrls(SimpleTestCase):
	def test_HomePage_url_is_resolved(self):
		url = reverse('mainapp:home-page')
		# print(resolve(url))
		self.assertEquals(resolve(url).func.__name__, HomePage.as_view().__name__)

	def test_NewsPage_url_is_resolved(self):
		url = reverse('mainapp:news-page')
		self.assertEquals(resolve(url).func.__name__, NewsPage.as_view().__name__)

	# another type of fix for unit test
	def test_NewsAllPage_url_is_resolved(self):
		url = reverse('mainapp:news-all')
		self.assertEquals(resolve(url).func.view_class, NewsAllPage)

	def test_postdetailpage_url_is_resolved(self):
		url = reverse('mainapp:post-detail', args=['some-str'])
		self.assertEquals(resolve(url).func.view_class, PostDetailPage)

	def test_AboutPage_url_is_resolved(self):
		url = reverse('mainapp:about-page')
		self.assertEquals(resolve(url).func.view_class, AboutPage)

	def test_SupportUs_url_is_resolved(self):
		url = reverse('mainapp:support-us-page')
		self.assertEquals(resolve(url).func.view_class, SupportUs)

	def test_DownloadPage_url_is_resolved(self):
		url = reverse('mainapp:download-page')
		self.assertEquals(resolve(url).func.view_class, DownloadPage)

	def test_ContactPage_url_is_resolved(self):
		url = reverse('mainapp:contact-page')
		self.assertEquals(resolve(url).func.view_class, ContactPage)

	def test_ConfirmPage_url_is_resolved(self):
		url = reverse('mainapp:confirm-contact-page')
		self.assertEquals(resolve(url).func.view_class, ConfirmPage)

	def test_SecurityContactPage_url_is_resolved(self):
		url = reverse('mainapp:secutiry-report-bug')
		self.assertEquals(resolve(url).func.view_class, SecurityContactPage)

	def test_SuccessSecurityPage_url_is_resolved(self):
		url = reverse('mainapp:secutiry-report-success')
		self.assertEquals(resolve(url).func.view_class, SuccessSecurityPage)



