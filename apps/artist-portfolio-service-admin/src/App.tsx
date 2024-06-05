import React, { useEffect, useState } from "react";
import { Admin, DataProvider, Resource } from "react-admin";
import buildGraphQLProvider from "./data-provider/graphqlDataProvider";
import { theme } from "./theme/theme";
import Login from "./Login";
import "./App.scss";
import Dashboard from "./pages/Dashboard";
import { CategoryList } from "./category/CategoryList";
import { CategoryCreate } from "./category/CategoryCreate";
import { CategoryEdit } from "./category/CategoryEdit";
import { CategoryShow } from "./category/CategoryShow";
import { ArtworkList } from "./artwork/ArtworkList";
import { ArtworkCreate } from "./artwork/ArtworkCreate";
import { ArtworkEdit } from "./artwork/ArtworkEdit";
import { ArtworkShow } from "./artwork/ArtworkShow";
import { PortfolioList } from "./portfolio/PortfolioList";
import { PortfolioCreate } from "./portfolio/PortfolioCreate";
import { PortfolioEdit } from "./portfolio/PortfolioEdit";
import { PortfolioShow } from "./portfolio/PortfolioShow";
import { ArtistList } from "./artist/ArtistList";
import { ArtistCreate } from "./artist/ArtistCreate";
import { ArtistEdit } from "./artist/ArtistEdit";
import { ArtistShow } from "./artist/ArtistShow";
import { jwtAuthProvider } from "./auth-provider/ra-auth-jwt";

const App = (): React.ReactElement => {
  const [dataProvider, setDataProvider] = useState<DataProvider | null>(null);
  useEffect(() => {
    buildGraphQLProvider
      .then((provider: any) => {
        setDataProvider(() => provider);
      })
      .catch((error: any) => {
        console.log(error);
      });
  }, []);
  if (!dataProvider) {
    return <div>Loading</div>;
  }
  return (
    <div className="App">
      <Admin
        title={"ArtistPortfolioService"}
        dataProvider={dataProvider}
        authProvider={jwtAuthProvider}
        theme={theme}
        dashboard={Dashboard}
        loginPage={Login}
      >
        <Resource
          name="Category"
          list={CategoryList}
          edit={CategoryEdit}
          create={CategoryCreate}
          show={CategoryShow}
        />
        <Resource
          name="Artwork"
          list={ArtworkList}
          edit={ArtworkEdit}
          create={ArtworkCreate}
          show={ArtworkShow}
        />
        <Resource
          name="Portfolio"
          list={PortfolioList}
          edit={PortfolioEdit}
          create={PortfolioCreate}
          show={PortfolioShow}
        />
        <Resource
          name="Artist"
          list={ArtistList}
          edit={ArtistEdit}
          create={ArtistCreate}
          show={ArtistShow}
        />
      </Admin>
    </div>
  );
};

export default App;
